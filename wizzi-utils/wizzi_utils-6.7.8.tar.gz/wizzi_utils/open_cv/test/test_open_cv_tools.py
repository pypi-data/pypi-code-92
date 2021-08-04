from wizzi_utils.misc import misc_tools as mt
from wizzi_utils.misc.test import test_misc_tools as mtt
from wizzi_utils.open_cv import open_cv_tools as cvt
from wizzi_utils.socket import socket_tools as st
from wizzi_utils.pyplot import pyplot_tools as pyplt
import numpy as np
import os
# noinspection PyPackageRequirements
import cv2

LOOP_TESTS = 50
BLOCK_MS_NORMAL = 2000  # 0 to block
ITERS_CAM_TEST = 10  # 0 to block


def load_img_from_web(name: str, ack: bool = True) -> np.array:
    f = mtt.IMAGES_INPUTS
    url = mtt.IMAGES_D[name]
    suffix = 'jpg'  # default
    # if '.webm' in url:
    #     suffix = 'webm'
    dst = '{}/{}.{}'.format(f, name, suffix)

    if not os.path.exists(dst):
        if not os.path.exists(f):
            mt.create_dir(f)
        success = st.download_file(url, dst)
        if not success:
            mt.exception_error('download failed - creating random img', real_exception=False)
            img = mt.np_random_integers(size=(240, 320, 3), low=0, high=255)
            img = img.astype('uint8')
            cvt.save_img(dst, img)

    img = cvt.load_img(path=dst, ack=ack)
    return img


def get_vid_from_web(name: str) -> str:
    f = mtt.VIDEOS_INPUTS
    url = mtt.VIDEOS_D[name]
    suffix = 'mp4'  # default
    if '.webm' in url:
        suffix = 'webm'
    dst = '{}/{}.{}'.format(f, name, suffix)

    if not os.path.exists(dst):
        if not os.path.exists(f):
            mt.create_dir(f)
        success = st.download_file(url, dst)
        if not success:
            mt.exception_error('download failed - creating random img', real_exception=False)
            dst = None

    return dst


def get_cv_version_test():
    mt.get_function_name(ack=True, tabs=0)
    cvt.get_cv_version(ack=True, tabs=1)
    return


def imread_imwrite_test():
    mt.get_function_name(ack=True, tabs=0)
    name = mtt.SO_LOGO
    img = load_img_from_web(name)

    f = mtt.IMAGES_INPUTS
    url = mtt.IMAGES_D[name]
    dst_path = '{}/{}'.format(f, os.path.basename(url).replace('.png', '_copy.png'))

    cvt.save_img(dst_path, img, ack=True)
    img_loaded = cvt.load_img(dst_path, ack=True)
    print(mt.to_str(img_loaded, '\timg_copy'))
    mt.delete_file(dst_path, ack=True)
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def list_to_cv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    img_list = img.tolist()
    print(mt.to_str(img_list, '\timg_list'))
    img = cvt.list_to_cv_image(img_list)
    print(mt.to_str(img, '\timg'))
    # mt.delete_file(file=mtt.TEMP_IMAGE_PATH, ack=True)
    return


def display_open_cv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    print('\tVisual test: stack overflow logo')
    loc = (70, 200)  # move to X,Y
    resize = 1.7  # enlarge to 170%
    cvt.display_open_cv_image(
        img=img,
        ms=1,  # not blocking
        title='stack overflow logo moved to {} and re-sized to {}'.format(loc, resize),
        loc=loc,  # start from x =70 y = 0
        resize=resize
    )
    loc = pyplt.Location.TOP_RIGHT.value  # move to top right corner
    resize = 1.7  # enlarge to 170%
    cvt.display_open_cv_image(
        img=img,
        ms=BLOCK_MS_NORMAL,  # blocking
        title='stack overflow logo moved to {} and re-sized to {}'.format(loc, resize),
        loc=loc,  # start from x =70 y = 0
        resize=resize
    )
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def display_open_cv_image_loop_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    loc = (70, 200)  # move to X,Y
    resize = 1.7  # enlarge to 170%
    title = 'stack overflow logo moved to {} and re-sized to {} - {} iterations'.format(loc, resize, LOOP_TESTS)
    print('\tVisual test: {}'.format(title))
    for i in range(LOOP_TESTS):
        cvt.display_open_cv_image(
            img=img,
            ms=1,  # not blocking
            title=title,
            loc=loc,  # start from x =70 y = 0
            resize=resize
        )
        if i == 0:  # move just first iter
            loc = None
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def resize_opencv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img1 = load_img_from_web(mtt.SO_LOGO)
    img2 = img1.copy()
    img3 = img1.copy()

    cvt.display_open_cv_image(
        img=img1,
        ms=1,
        title='img1',
        loc=pyplt.Location.TOP_LEFT.value,
        resize=1.6,
        header='resize to 160%',
        save_path=None,
    )
    cvt.display_open_cv_image(
        img=img2,
        ms=BLOCK_MS_NORMAL,
        title='img2',
        loc=pyplt.Location.CENTER_LEFT.value,
        resize=(400, 200),
        header='resize to (400, 200)',
        save_path=None,
    )
    cv2.destroyAllWindows()

    # no full-screen
    cvt.display_open_cv_image(
        img=img3,
        ms=BLOCK_MS_NORMAL,
        title='img3',
        loc=pyplt.Location.BOTTOM_LEFT.value,
        resize='fs',
        header='resize to full-screen',
        save_path=None,
    )
    cv2.destroyAllWindows()
    return


def move_cv_img_x_y_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    options = [(0, 0), (100, 0), (0, 100), (150, 150), (400, 400), (250, 350)]
    print('\tVisual test: move to all options {}'.format(options))
    print('\t\tClick Esc to close all')
    for x_y in options:
        title = 'move to ({})'.format(x_y)
        cv2.imshow(title, img)
        cvt.move_cv_img_x_y(title, x_y)
    cv2.waitKey(BLOCK_MS_NORMAL)
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def move_cv_img_by_str_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    options = pyplt.Location.get_location_list_by_rows()
    print('\tVisual test: move to all options {}'.format(options))
    print('\t\tClick Esc to close all')
    for where_to in options:
        title = 'move to {}'.format(where_to)
        cv2.imshow(title, img)
        cvt.move_cv_img_by_str(img, title, where=where_to)
    cv2.waitKey(BLOCK_MS_NORMAL)
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def unpack_list_imgs_to_big_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    gray = cvt.BGR_img_to_gray(img)
    big_img = cvt.unpack_list_imgs_to_big_image(
        imgs=[img, gray, img],
        grid=(2, 2)
    )
    title = 'stack overflow logo 2x2(1 empty)'
    print('\tVisual test: {}'.format(title))
    cvt.display_open_cv_image(
        img=big_img,
        ms=BLOCK_MS_NORMAL,  # blocking
        title=title,
        loc=(0, 0),
        resize=None
    )
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def display_open_cv_images_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    title = '2x1 grid'
    print('\tVisual test: {}'.format(title))
    loc1 = (0, 0)
    cvt.display_open_cv_images(
        imgs=[img, img],
        ms=1,  # blocking
        title='{} loc={}'.format(title, loc1),
        loc=loc1,
        resize=1.5,
        grid=(2, 1),
        header='{} loc={}'.format(title, loc1),
    )
    loc2 = pyplt.Location.BOTTOM_CENTER.value
    cvt.display_open_cv_images(
        imgs=[img, img],
        ms=BLOCK_MS_NORMAL,  # blocking
        title='{} loc={}'.format(title, loc2),
        loc=loc2,
        resize=None,
        grid=(2, 1),
        header='{} loc={}'.format(title, loc1),
    )
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def display_open_cv_images_loop_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    loc = (70, 200)  # move to X,Y
    title = 'stack overflow logo moved to {} - {} iterations'.format(loc, LOOP_TESTS)
    print('\tVisual test: {}'.format(title))
    for i in range(LOOP_TESTS):
        cvt.display_open_cv_images(
            imgs=[img, img],
            ms=1,  # blocking
            title=title,
            loc=loc,
            resize=None,
            grid=(2, 1),
            header=None
        )
        if i == 0:  # move just first iter
            loc = None
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def gray_to_BGR_and_back_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.SO_LOGO)
    print(mt.to_str(img, '\timgRGB'))
    gray = cvt.BGR_img_to_gray(img)
    print(mt.to_str(img, '\timg_gray'))
    img = cvt.gray_scale_img_to_BGR_form(gray)
    print(mt.to_str(img, '\timgRGB'))
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def BGR_img_to_RGB_and_back_test():
    mt.get_function_name(ack=True, tabs=0)
    imgBGR1 = load_img_from_web(mtt.SO_LOGO)
    print(mt.to_str(imgBGR1, '\timgBGR'))
    imgRGB = cvt.BGR_img_to_RGB(imgBGR1)
    print(mt.to_str(imgRGB, '\timgRGB'))
    imgBGR2 = cvt.RGB_img_to_BGR(imgRGB)
    print(mt.to_str(imgBGR2, '\timgBGR2'))

    cvt.display_open_cv_images(
        imgs=[imgBGR1, imgRGB, imgBGR2],
        ms=BLOCK_MS_NORMAL,  # blocking
        title='imgBGR1, imgRGB, imgBGR2',
        loc=pyplt.Location.CENTER_CENTER,
        resize=None,
        grid=(3, 1),
        header='compare'
    )
    cv2.destroyAllWindows()
    # mt.delete_file(file=mtt.SO_LOGO_PATH, ack=True)
    return


def CameraWu_test(type_cam: str):
    WITH_SLEEP = False
    ports = [0, 1, 13]
    cams = []
    for port in ports:
        cam = cvt.CameraWu.open_camera(port=port, type_cam=type_cam)
        if cam is not None:
            cams.append(cam)

    for cam in cams:
        title = 'CameraWu_test({}) on port {}'.format(cam.type_cam, cam.port)
        fps = mt.FPS(summary_title=title)
        for i in range(ITERS_CAM_TEST):
            fps.start()
            success, cv_img = cam.read_img()
            if WITH_SLEEP:
                mt.sleep(1)

            if success:
                cvt.display_open_cv_image(
                    img=cv_img,
                    ms=1,
                    title=title,
                    loc=pyplt.Location.CENTER_CENTER,
                    resize=None,
                    header='{}/{}'.format(i + 1, ITERS_CAM_TEST)
                )
            fps.update()
        fps.finalize()
    cv2.destroyAllWindows()
    return


def CameraWu_cv2_test():
    mt.get_function_name(ack=True, tabs=0)
    CameraWu_test(type_cam='cv2')
    return


def CameraWu_acapture_test():
    mt.get_function_name(ack=True, tabs=0)
    CameraWu_test(type_cam='acapture')
    return


def CameraWu_imutils_test():
    mt.get_function_name(ack=True, tabs=0)
    CameraWu_test(type_cam='imutils')
    return


def add_text_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.HORSES)
    cvt.add_text(img, header='test text', pos=(100, 100), text_color='r', with_rect=True, bg_color='y', bg_font_scale=2)
    cvt.add_text(img, header='test text', pos=(100, 200), text_color='black', with_rect=True, bg_color='b',
                 bg_font_scale=1)
    cvt.display_open_cv_image(img, ms=BLOCK_MS_NORMAL, loc=pyplt.Location.CENTER_CENTER.value)
    cv2.destroyAllWindows()
    return


def add_header_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web(mtt.HORSES)

    cvt.add_header(img, header='TOP_LEFT', loc=pyplt.Location.TOP_LEFT.value,
                   text_color='lime', with_rect=True, bg_color='azure', bg_font_scale=1)
    cvt.add_header(img, header='BOTTOM_LEFT', loc=pyplt.Location.BOTTOM_LEFT.value,
                   text_color='fuchsia', with_rect=True, bg_color='black', bg_font_scale=2)
    cvt.add_header(img, header='TOP_RIGHT', loc=pyplt.Location.TOP_RIGHT.value, x_offset=180,
                   text_color='darkorange', with_rect=True, bg_color='azure', bg_font_scale=1)
    cvt.add_header(img, header='BOTTOM_RIGHT', loc=pyplt.Location.BOTTOM_RIGHT.value, x_offset=120,
                   text_color='aqua', with_rect=True, bg_color='black', bg_font_scale=2)
    cvt.display_open_cv_image(img, title='all headers', ms=1, loc=pyplt.Location.TOP_LEFT.value)

    img = load_img_from_web(mtt.DOG)
    cvt.display_open_cv_image(
        img,
        title='built in header',
        ms=BLOCK_MS_NORMAL,
        loc=pyplt.Location.TOP_RIGHT.value,
        header='direct header into display_open_cv_image'
    )
    cv2.destroyAllWindows()
    return


def Mp4_creator_test():
    mt.get_function_name(ack=True, tabs=0)
    # now open video file
    vid_name = mtt.DOG1
    video_path = get_vid_from_web(name=vid_name)

    if not os.path.exists(video_path):
        mt.exception_error(mt.NOT_FOUND.format(video_path), real_exception=False)
        return
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        out_dims = cvt.get_dims_from_cap(cap)
        video_total_frames = cvt.get_frames_from_cap(cap)
        print('\tvid {} has {} frames'.format(vid_name, video_total_frames))
        print('\tvid size is {}'.format(out_dims))
    else:
        mt.exception_error('cap is closed.', real_exception=False)
        return

    out_dir = '{}/create_mp4_test'.format(mtt.VIDEOS_OUTPUTS)
    mt.create_dir(out_dir)
    out_fp = '{}/{}_output.mp4'.format(out_dir, vid_name)

    mp4_creator = cvt.Mp4_creator(
        out_full_path=out_fp,
        out_fps=20.0,
        out_dims=out_dims
    )
    print(mp4_creator)

    for i in range(video_total_frames):
        success, frame = cap.read()
        if i % int(video_total_frames / 10) != 0:  # s
            # do only 10 frames
            continue
        print('\tframe {}/{}:'.format(i + 1, video_total_frames))
        # print('\t\t{}'.format(mt.to_str(frame)))
        if success:
            cvt.add_header(
                frame,
                header='create_mp4_test frame {}/{}'.format(i + 1, video_total_frames),
                loc=pyplt.Location.BOTTOM_LEFT.value,
                text_color=pyplt.get_random_color(),
                bg_color=pyplt.get_random_color(),
            )
            cvt.display_open_cv_image(frame, ms=1, title=vid_name, loc=None,
                                      header='{}/{}'.format(i + 1, video_total_frames))
            mp4_creator.add_frame(frame, ack=True, tabs=2)

    cap.release()
    mp4_creator.finalize()
    cv2.destroyAllWindows()
    return


def get_aspect_ratio_test():
    mt.get_function_name(ack=True, tabs=0)
    cv_img_fake = np.zeros(shape=(480, 640, 3))
    img_h, img_w = cv_img_fake.shape[0], cv_img_fake.shape[1]
    new_h = 192
    resize_dims = cvt.get_aspect_ratio_w(img_w=img_w, img_h=img_h, new_h=new_h)
    print('\timage size={} and new_h={}: new dims should be {}'.format(cv_img_fake.shape, new_h, resize_dims))

    new_w = 192
    resize_dims = cvt.get_aspect_ratio_h(img_w=img_w, img_h=img_h, new_w=new_w)
    print('\timage size={} and new_w={}: new dims should be {}'.format(cv_img_fake.shape, new_w, resize_dims))
    return


def cuda_on_gpu_test():
    """
    opencv cuda installation on WINDOWS 10:
    youtube https://www.youtube.com/watch?v=YsmhKar8oOc&ab_channel=TheCodingBug
    ** all links for download in the link
    ** in brackets: my specific installation
    * install anaconda
    * vs studio 19 with "desktop development C++" and "python development"
    * Cuda toolkit (cuda toolkit 10.2)
    * cuDNN - version that match the cuda toolkit above (cuDnn v7.6.5 for Cuda 10.2)
        * archive: https://developer.nvidia.com/rdp/cudnn-archive
        * copy all to cuda (bin to bin, lib to lib, include to include)
        * minimum 7.5
    * CMake
    * openCV source (4.5.2)
    * openCV contrib - same version as openCV above (4.5.2)
        * place openCV and openCV contrib in the same folder and extract both

    1 build a new python env anywhere(conda(base or custom), normal py, venv...)
    2 set 4 system environment variables:
        let PY_PATH be you python dir (conda env, normal py, venv...)
        go to PATH and add the next 4:
            * PY_PATH # for the python.exe
            * PY_PATH/Scripts # for pip...
            * PY_PATH/libs  # for python36.lib file
            * PY_PATH/include # h files
    2b pip install numpy (if you want tf, 1.19.5)
    3 open CMake gui
    * source code: location of openCV source
    * create 2 new dirs in the level of openCV source called build and install
    * where to build: location of build folder created above
    * configure, set generator x64 and finish
    * click grouped checkbox and look in PYTHON3
        should have EXECUTABLE, INCLUDE_DIR, LIBRARY, NUMPY_INCLUDE, PACKAGES paths filled according to PY_PATH
        look at the output and search for OpenCV modules. if python3 in Unavailable - don't continue. it should be
        in the "To be built"
    * extra round of flags:
        WITH_CUDA
        BUILD_opencv_dnn
        OPENCV_DNN_CUDA
        ENABLE_FAST_MATH
        BUILD_opencv_world
        BUILD_opencv_python3 # should already be on
        OPENCV_EXTRA_MODULES_PATH -> set to openCV contrib on modules folder
    * hit configure - in the output you should see your CUDA and cuDNN details
        CUDA detected: x.y (10.2)
        Found CUDNN path ...
    * extra round of flags:
        CUDA_FAST_MATH
        CUDA_ARCH_BIN -> go to https://en.wikipedia.org/wiki/CUDA and look for your GPU. find it's Compute
            capability (version). (my GPU is gtx 1050. version 6.1)
            remove all versions other than you GPU version. (i left only 6.1)
        CMAKE_INSTALL_PREFIX -> place install path from above (you create this dir with build above)
        CMAKE_CONFIGURATION_TYPES -> remove Debug and keep only Release
    * hit configure
    * hit generate
    close CMAKE gui
    4 go to build folder and look for OpenCV.sln
    * goto solution explorer->CMakeTargets-> right click ALL_BUILD and hit build # should take 10-30 mins
    * if done with no errors, right click INSTALL and build.
    * if no errors, openCV cuda is ready
    5 validation: open terminal and write python (should work due to step 2)
    import cv2
    print(cv2.__version__)
    print(cv2.cuda.getCudaEnabledDeviceCount())  # should be >=1
    run this main (cuda open cv test)
    6 cleanup
    * delete all build folder except build/lib # maybe for future use ?
    * delete both zips and extracted open cv and open cv contrib
    7 after checking on pycharm, open cv with GPU support should work but no autocomplete.
    pip install mypy
    stubgen -m cv2 -o ENV_PATH\Lib\site-packages\cv2
    # if the stubgen fails, run as administrator
    # rename cv2.pyi created to __init__.pyi
    # all done
    e.g:
    stubgen -m cv2 -o C:\\Users\\GiladEiniKbyLake\\.conda\\envs\\cv_cuda\\Lib\\site-packages\\cv2
    # a file was created at C:\\Users\\GiladEiniKbyLake\\.conda\\envs\\temp\\Lib\\site-packages\\cv2\\cv2.pyi
    # rename cv2.pyi to __init__.pyi and have the file:
        C:\\Users\\GiladEiniKbyLake\\.conda\\envs\\temp\\Lib\\site-packages\\cv2\\__init__.pyi
    :return:
    """
    mt.get_function_name(ack=True, tabs=0)
    print(cvt.get_cv_version())
    gpus = cvt.get_gpu_devices_count()
    print('\t{} GPU devices detected'.format(gpus))
    if gpus > 0:
        npTmp = np.random.random((1024, 1024)).astype(np.float32)

        npMat1 = np.stack([npTmp, npTmp], axis=2)
        npMat2 = npMat1

        cuMat1 = cv2.cuda_GpuMat()
        cuMat2 = cv2.cuda_GpuMat()
        cuMat1.upload(npMat1)
        cuMat2.upload(npMat2)
        # start_time = time.time()
        start_time = mt.get_timer()
        # noinspection PyUnresolvedReferences
        cv2.cuda.gemm(cuMat1, cuMat2, 1, None, 0, None, 1)
        print("\t\tCUDA --- %s seconds ---" % (mt.get_timer() - start_time))
        # start_time = time.time()
        start_time = mt.get_timer()

        cv2.gemm(npMat1, npMat2, 1, None, 0, None, 1)
        print("\t\tCPU  --- %s seconds ---" % (mt.get_timer() - start_time))
    return


def test_all():
    print('{}{}:'.format('-' * 5, mt.get_base_file_and_function_name()))
    get_cv_version_test()
    imread_imwrite_test()
    list_to_cv_image_test()
    display_open_cv_image_test()
    display_open_cv_image_loop_test()
    resize_opencv_image_test()
    move_cv_img_x_y_test()
    move_cv_img_by_str_test()
    unpack_list_imgs_to_big_image_test()
    display_open_cv_images_test()
    display_open_cv_images_loop_test()
    gray_to_BGR_and_back_test()
    BGR_img_to_RGB_and_back_test()
    add_header_test()
    add_text_test()
    CameraWu_cv2_test()
    CameraWu_acapture_test()
    CameraWu_imutils_test()
    Mp4_creator_test()
    get_aspect_ratio_test()
    cuda_on_gpu_test()
    print('{}'.format('-' * 20))
    return
