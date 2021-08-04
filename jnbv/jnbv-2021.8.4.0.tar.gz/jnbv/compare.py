import difflib
import logging
import os
import json

from .read import read_ipynb
from .test import assert_no_errors
from .utils import BLUE, CYAN, GREEN, LIGHTPURPLE, NC, RED, \
    print_cropped_output


def compare_ipynb_notebooks(notebook_filenames, debug):
    """Compare sources and outputs in two notebooks.
    Return True or False and any errors found."""

    # Print and log what is going to happen
    print("")
    print(LIGHTPURPLE, "*".center(80, "*"), NC)
    print(LIGHTPURPLE, "Comparing outputs of:", NC)
    print("  ", str(notebook_filenames[0]) + "\n  ",
          str(notebook_filenames[1]))
    print("")
    logging.info("Comparing outputs of " + str(notebook_filenames[0]))
    logging.info(str(notebook_filenames[1]))

    # Return values
    comparison_result = False
    comparison_errors = []
    error_message = ""
    error_content = ""

    # First read the ipynb notebooks into python dictionaries
    notebook_output = []
    for notebook_filename in notebook_filenames:
        nb, errors = read_ipynb(notebook_filename, True, debug)
        notebook_output.append(nb)

        # Check for empty notebooks
        if "cells" not in nb:
            error_message = "EMPTY NOTEBOOK!"
            print(RED, error_message)
            logging.error(error_message)
            return comparison_result, error_message, error_content

    # Check if numbers of cells in the notebooks is different
    if len(notebook_output[0].cells) != len(notebook_output[1].cells):
        error_message = "number of cells is different in the two notebooks"
        print(RED, error_message)
        logging.error(error_message)
        return comparison_result, error_message, error_content

    # Loop over the cells in the notebooks
    for cells in zip(notebook_output[0].cells, notebook_output[1].cells):

        # Comparisons only made for source cells that contain code and are
        # not empty
        if should_cells_be_compared(cells[0], cells[1], debug):

            # Check if source cells are the same or if they contain
            # special keywords
            ignore_output_differences, source_errors = \
                compare_source_lines(
                    cells[0]["source"], cells[1]["source"], debug
                )
            comparison_errors.extend(source_errors)

            len_0_output = len(cells[0]["outputs"])
            len_1_output = len(cells[1]["outputs"])

            # Empty output is not necessarily bad, print it
            (len_0_output == 0 or len_1_output == 0) and \
                print(BLUE, "-".center(80, "-"), NC)
            len_0_output == 0 and print(CYAN, "cells[0][outputs]: ", NC) \
                and print_cropped_output(cells[0]["outputs"])
            len_1_output == 0 and print(CYAN, "cells[1][outputs]: ", NC) \
                and print_cropped_output(cells[1]["outputs"])
            (len_0_output == 0 or len_1_output == 0) and \
                print(BLUE, "-".center(80, "-"), NC)

            # # NOTE: Commented out this seciton 2021-05-26, need to
            #         think more about it...
            # # Check if size of the output arrays are different
            # if len_0_output != len_1_output:
            #     message = "output sizes not the same"
            #     print(RED, message, NC)
            #     print(len_0_output)
            #     for output in cells[0]["outputs"]:
            #         print("  ", output)
            #     print(len_1_output)
            #     for output in cells[1]["outputs"]:
            #         print("  ", output)
            #     logging.error(message)
            #     comparison_errors.append(cells[0]["outputs"])
            #     comparison_errors.append(cells[1]["outputs"])

            # Loop over outputs - can have multiple for each source cell
            for outputs in zip(cells[0]["outputs"], cells[1]["outputs"]):

                print(BLUE, "-".center(80, "-"), NC)

                # Print the output lines
                for idx, output in enumerate(outputs):
                    logging.info("outputs[" + str(idx) + "] : " +
                                 str(output))
                    print(CYAN, "outputs[", str(idx), "]: ", NC)
                    # Crop long output (e.g. images) to terminal
                    print_cropped_output(output)

                print(BLUE, "-".center(80, "-"), NC)

                if outputs[0] == outputs[1]:
                    print(GREEN)
                    message = "outputs are the same"

                else:
                    # Some differences can be ignored - look closer for those
                    comparison_pass = examine_output_diff(
                        ignore_output_differences, outputs[0], outputs[1],
                        debug
                    )

                    if comparison_pass:
                        print(GREEN)
                        message = "outputs are almost the same"
                    else:
                        print(RED)
                        message = "outputs are not the same"
                        comparison_errors.append(outputs[0])
                        comparison_errors.append(outputs[1])

                print(message, NC)
                logging.info(message)

    # Check comparisons for errors (differences)
    comparison_result, error_message, error_content = \
        check_for_errors(comparison_errors)

    return comparison_result, error_message, error_content


def check_for_errors(comparison_errors):

    comparison_result = False
    error_message = ""
    error_content = ""

    try:
        comparison_result = assert_no_errors(comparison_errors)
        comparison_result = True
    except AssertionError as e:
        error_message = "AssertionError"
        error_content = e
    except BaseException as e:
        error_message = "Unknown Error"
        error_content = e

    return comparison_result, error_message, error_content


def print_comparison_results(notebook_filenames, comparison_result,
                             error_message, error_content, debug):

    # Print & log errors
    if error_message != "":
        print("\n", RED, error_message, "\n", error_content)
        logging.error(error_message)
        logging.error(error_content)
    print(GREEN) if comparison_result else print(RED)
    print("-".center(80, "-"))
    print(" comparison result: " + str(comparison_result))
    print("-".center(80, "-"), NC)

    # Log results
    logging.info("comparison result: " + str(comparison_result))
    logging.info("Done Comparing outputs of ")
    logging.info(str(notebook_filenames[0]))
    logging.info(str(notebook_filenames[1]))

    # Print results
    print("")
    print(LIGHTPURPLE, "Done Comparing outputs of:", NC)
    print("  " + str(notebook_filenames[0]) + "\n" "  " +
          str(notebook_filenames[1]))
    print(LIGHTPURPLE, "*".center(80, "*"), NC)
    print("")

    return comparison_result


def should_cells_be_compared(cells_0, cells_1, debug):
    """Check to see if source cell is code, is not empty"""

    debug and print("cells_0:", cells_0, "\n", "cells_1:", cells_1)

    if "cell_type" not in cells_0 or "cell_type" not in cells_1:
        return False

    # Only continue for code, skip comments/markdown
    if cells_0["cell_type"] != "code" or cells_1["cell_type"] != "code":
        return False

    # Check that both source and output cells exist in the
    # notebooks
    if "source" not in cells_0 or "outputs" not in cells_0 \
            or "source" not in cells_1 or "outputs" not in cells_0:
        return False

    # Check for empty cells
    if cells_0["source"] == "" or cells_1["source"] == "":
        return False

    return True


def compare_source_lines(source_line_0, source_line_1, debug):

    # Some output for given sources can be ignored, e.g. output from timing
    # finctions will not be exactly the same
    ignore_output_if_source = ["timeit", "random_directions"]
    ignore_output_differences = False

    # Look at the source lines
    logging.info("source_line_0: " + str(source_line_0))
    logging.info("source_line_1: " + str(source_line_1))

    print(BLUE, "-".center(80, "-"), NC)
    print(BLUE, "source_line_0: ", NC, source_line_0)
    print(BLUE, "source_line_1: ", NC, source_line_1)
    print(BLUE, "-".center(80, "-"), NC)

    # Compare the two source lines
    message = ""
    comparison_errors = []
    if source_line_0 == source_line_1:
        message = "sources are the same"
        print(GREEN)

        # Ignore output from certain sources
        for source_item in ignore_output_if_source:
            if source_item in source_line_0:
                ignore_output_differences = True
    else:
        message = "sources are not the same"
        print(RED)
        comparison_errors.append(source_line_0)
        comparison_errors.append(source_line_1)
        logging.error(message)
    print(message, NC)
    print("")

    return ignore_output_differences, comparison_errors


def examine_output_diff(ignore_output_differences, nb0, nb1, debug):
    """Look closer at differences between output from two notebooks"""

    debug and print(GREEN, "** Entering examine_output_diff **", NC,
                    "\n", CYAN, type(nb0), NC, "\n", CYAN, type(nb1), NC)

    if ignore_output_differences:
        return True

    comparison_pass = True

    # Some keys, subkeys, and values to be ignored
    keys_to_look_for = ["data", "execution_count", "text"]
    keys_to_ignore = ["execution_count"]

    # Loop over all keys in the first dictionary
    for key in nb0:

        debug and print(BLUE, "  key:", NC, key)

        # Check if the values are the same for the same key in the two
        # dictionaries
        if key not in nb1:
            comparison_pass = False
            debug and print(RED, "comparison_pass: ", comparison_pass, NC,
                            RED, "\n    key ", key, "not in nb1", NC)

        else:
            # The easy case - values are exactly the same, nothing more to do
            if nb0[key] == nb1[key]:
                debug and print(GREEN, "    same key values", NC)

            else:
                debug and print(RED, "    different key values", NC)

                # If the values are different, take a closer look - maybe this
                # difference can be ignored
                if key in keys_to_look_for:

                    # For certain keys, completely ignore differences in the
                    # values
                    key in keys_to_ignore and debug and print(GREEN, "ignore ",
                                                              key, NC)

                    # For other keys, ignore certain differences in the values
                    if key == "data":
                        key_data_comparison_pass = examine_output_key_data(
                            key, nb0, nb1, debug
                        )
                        if not key_data_comparison_pass:
                            comparison_pass = False

                    if key == "text":
                        key_text_comparison_pass = examine_output_key_text(
                            key, nb0, nb1, debug
                        )
                        if not key_text_comparison_pass:
                            comparison_pass = False

                else:
                    comparison_pass = False
                    debug and print(RED, "comparison_pass: ", comparison_pass,
                                    NC, RED, "\n    key ", key,
                                    "not in keys_to_look_for", NC)

    debug and print("comparison_pass: ", comparison_pass, GREEN,
                    "\n** Leaving examine_output_diff **", NC)

    return comparison_pass


def examine_output_key_data(key, nb0, nb1, debug):

    comparison_pass = True

    subkey_values_to_ignore = {}
    subkey_values_to_ignore["data"] = {
        "text/html": ["h5glance", "image/png"],
        "application/vnd.jupyter.widget-view+json": ["model_id"],
        "text/plain": ["h5glance", "matplotlib."],
    }

    for subkey in nb0[key]:

        if nb0[key][subkey] == nb1[key][subkey]:
            debug and print(BLUE, "    --> subkey:", NC, subkey,
                            "\n", GREEN, "      same subkey values", NC)
        else:
            debug and print(BLUE, "    --> subkey:", NC, subkey,
                            RED, "\n      different subkey values", NC)

            # For images, sometimes they were not exactly the same, though
            # could not tell by eye - should investigate further perhaps?
            if subkey == "image/png":
                if not compare_images(nb0[key][subkey], nb1[key][subkey],
                                      debug):
                    return False

            else:
                # For certain sub-keys, ignore differences
                # in the values
                if subkey not in subkey_values_to_ignore[key]:
                    debug and print(RED, "    subkey not in ",
                                    "subkey_values_to_ignore", "[key]", NC)
                    return False

                found_subkey_to_ignore = False
                for subkey_value in subkey_values_to_ignore[key][subkey]:
                    if subkey_value in nb0[key][subkey]:
                        found_subkey_to_ignore = True
                        debug and print(GREEN, "       ignoring...",
                                        subkey_value, NC)
                comparison_pass = found_subkey_to_ignore

    return comparison_pass


def examine_output_key_text(key, nb0, nb1, debug):

    debug and print("Entered examine_output_key_text()")

    comparison_pass = True
    found_key_to_ignore = False

    key_values_to_ignore_AND = {}
    key_values_to_ignore_AND["text"] = [
        "Test: dtype:",
        "Elapsed Time",
        "CPU times",
        "INFO:dxchange.reader",
        "Reconstructing 1 slice groups",
        "liquid fraction",
        "R2019a",
        "Mpix",
        "Gflops",
        "naive GPU",
        "HDF5_PLUGIN_PATH",
        "VisibleDeprecationWarning",
        "MatplotlibDeprecationWarning",
        "Hello",
        "hello",
    ]

    key_values_to_ignore_OR = {}
    key_values_to_ignore_OR["text"] = [
        "R2019a",
        "HDF5_PLUGIN_PATH",
        "Hello",
        "hello"
    ]

    # Check for ouput which should always appear, but is most likely different,
    # such as the time to run some analysis cell
    if key in key_values_to_ignore_AND:
        for value in key_values_to_ignore_AND[key]:
            if value in nb0[key] and value in nb1[key]:
                found_key_to_ignore = True
        comparison_pass = found_key_to_ignore

    # Check for output which may occur but may not, like mention of the
    # hdf5 plugin path, which could be set or not, if another equivelant
    # module is loaded
    if key in key_values_to_ignore_OR:
        for value in key_values_to_ignore_OR[key]:
            if value in nb0[key] or value in nb1[key]:
                found_key_to_ignore = True
        comparison_pass = found_key_to_ignore

    # Check for the occaissional extra \r or \n
    if "\r" in nb0[key] or "\r" in nb1[key] or \
            "\n" in nb0[key] or "\n" in nb1[key]:
        if nb0[key].replace("\r", "") == nb1[key].replace("\r", "") or \
                nb0[key].replace("\n", "") == nb1[key].replace("\n", ""):
            comparison_pass = True

    if debug:
        print("      key: ", key)
        print("      values: ")
        print("         nb0[", key, "]: ", nb0[key])
        print("         nb1[", key, "]: ", nb1[key])
        print("      ignore", key, "differences:", comparison_pass)

    return comparison_pass


def compare_images(image_0, image_1, debug):
    """Sometimes images may look visually the same, but the png value if
    printed out is not the same.  Look to see if two images are
    close enough."""

    png_diff = difflib.SequenceMatcher(None, a=image_0, b=image_1).ratio()

    # This png difference doesn't seem too
    # reliable....
    image_comparison = True
    # if png_diff > 0.9:
    if png_diff > 0.00001:
        debug and print(GREEN, "        ignoring...", "png_diff: ", png_diff,
                        NC)
    else:
        image_comparison = False
        if debug:
            print(RED, "image_comparison: ", image_comparison, NC)
            print(RED, "    png_diff <= 0.9", ", png_diff: ", png_diff, NC)
    return image_comparison


def parse_input_names(input_notebook_filenames, debug):
    """Parse the input filenames string or list, return list"""

    # Input could be a long string of names, or a list
    notebook_filenames = []
    for input_notebook_filename in input_notebook_filenames:
        notebook_filenames.extend(input_notebook_filename.split())
    if debug:
        print("")
        print("Notebook Filenames:")
        print(json.dumps(notebook_filenames, indent=4))

    if notebook_filenames == []:
        print(RED, "At least one argument (one or more ipynb filenames)",
              "required\n", NC)
        assert False

    # Check if files exist, assert error if not
    files_exist = True
    for notebook_filename in notebook_filenames:
        if os.path.isfile(notebook_filename):
            debug and print(GREEN, notebook_filename, "exists", NC)
        else:
            print(RED, notebook_filename, "does not exist", NC)
            files_exist = False

    if not files_exist:
        print(RED, "One more more files do not exist\n", NC)
        assert False

    return notebook_filenames


def parse_compare_input(args_compare, args_execute, debug):
    """Parse the compare option input, output boolean or file name"""

    # The args_compare option can be one of the following:
    #   - null
    #   - an empty list
    #   - a list of file names
    # Output from this funcion will be one of:
    #   - True
    #   - False
    #   - file name
    if debug:
        print("args.compare is: ")
        print("    list:", isinstance(args_compare, list))
        print("    bool:", isinstance(args_compare, bool))
        print("     str:", isinstance(args_compare, str))

    if isinstance(args_compare, list):
        # Only take the first name in the list
        if len(args_compare) > 0:
            args_compare = args_compare[0]
        # The flag has been given, and the list is empty, then set to True
        else:
            args_compare = True
        return args_compare

    if args_compare is None:
        return False

    # If the option is a boolean, check if it makes sense to continue
    if isinstance(args_compare, bool):

        if args_compare and not args_execute:
            print(RED, "\nNo comparison to be made\n", NC)
            print(BLUE, "Example of comparing two files:", NC)
            print("    jnbv file1.ipynb --compare file2.ipynb")
            print(BLUE, "Example of executing a file, then comparing",
                  " the output with the original file:", NC)
            print("    jnbv file1.ipynb --kernel_name python3 --execute ",
                  "--compare\n")
            print(RED, "Assertion Error:", NC)
            assert False

    # If a file name has been given check that it exists
    if isinstance(args_compare, str):

        if os.path.isfile(args_compare):
            debug and print(GREEN, args_compare, "exists", NC)
        else:
            print(RED, args_compare, "does not exist\n", NC)
            assert False

    return args_compare


def dummy_test():
    return True
