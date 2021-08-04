# AUTOGENERATED! DO NOT EDIT! File to edit: 00_showdoc.ipynb (unless otherwise specified).

__all__ = ['show_doc', 'doc']

# Cell
from nbdev.showdoc import (
    _format_enum_doc, _format_cls_doc,
    _format_func_doc, add_doc_links,
    get_source_link, qual_name, is_enum,
    get_doc_link, md2html
)

import re

import inspect

from fastcore.foundation import Config
from fastcore.imports import IN_COLAB
from fastcore.utils import IN_NOTEBOOK

if IN_NOTEBOOK:
    from IPython.display import Markdown,display
    from IPython.core import page

# Cell
def _format_args(
    func:callable # Some callable function or class
):
    "Generate a doc string for `func`'s arguments"
    _pat = r'\((?P<args>.*)\)'
    try:
        source = inspect.getsource(func)
        arg_list = re.findall(_pat, source, flags=re.DOTALL)[0].split('\n')
        spec = inspect.getfullargspec(func)
        gt_spec = []
        for arg in spec.args: gt_spec.append(arg)
        if spec.varkw is not None: gt_spec.append(f'**{spec.varkw}')
        argstring = '**Function Arguments**:\n'
        has_arg = False
        for arg in arg_list:
            if len(arg.split('#')) > 1:
                # Contains argument documentation
                arg = arg.lstrip()
                if len(arg.split(':')) > 1:
                    arg_nm, extra = arg.split(':')
                    if arg_nm not in gt_spec: continue
                    else: has_arg = True
                    typ, arg_str = extra.split('#')
                    typ = typ.rstrip()
                    arg_str = arg_str.lstrip()
                    if '=' in typ: typ = typ.split('=')[0]
                    if typ.endswith(','): typ = typ[:-1]
                    typ_str = ''
                    if not typ[0].isalnum() and not typ[-1].isalnum():
                        typ = typ[1:-1]
                    typ_str = typ
                    argstring += f'* `{arg_nm}` (`{typ_str}`): {arg_str}\n'
                else:
                    # We don't have a type declaration
                    arg_nm, arg_str = arg.split('#')
                    arg_nm = arg_nm.rstrip()
                    arg_str = arg_str.lstrip()
                    if arg_nm.endswith(','): arg_nm = arg_nm[:-1]
                    if '=' in arg_nm: arg_nm = arg_nm.split('=')[0]
                    if arg_nm not in gt_spec: continue
                    else: has_arg = True
                    argstring += f'* `{arg_nm}`: {arg_str}\n'
        if has_arg: return argstring
        else: return ''
    except: return ''

# Cell
def show_doc(
    elt, # Some function or class to pull up the documentation for
    doc_string:bool=True, # Whether to display the doc string
    name:str=None, # An optional name to use instead
    title_level:int=None, # The heading level
    disp:bool=True, # Whether to display the Markdown
    default_cls_level:int=2 # If elt is a class, a heading level to use for it
):
    "Show documentation for element `elt` with potential verbose inputs. Supported types: class, function, and enum."
    elt = getattr(elt, '__func__', elt)
    qname = name or qual_name(elt)
    if inspect.isclass(elt):
        if is_enum(elt): name,args = _format_enum_doc(elt, qname)
        else:            name,args = _format_cls_doc (elt, qname)
    elif callable(elt):  name,args = _format_func_doc(elt, qname)
    else:                name,args = f"<code>{qname}</code>", ''
    link = get_source_link(elt)
    source_link = f'<a href="{link}" class="source_link" style="float:right">[source]</a>'
    title_level = title_level or (default_cls_level if inspect.isclass(elt) else 4)
    doc =  f'<h{title_level} id="{qname}" class="doc_header">{name}{source_link}</h{title_level}>'
    doc += f'\n\n> {args}\n\n' if len(args) > 0 else '\n\n'
    if doc_string and inspect.getdoc(elt):
        s = inspect.getdoc(elt)
        # show_doc is used by doc so should not rely on Config
        try: monospace = (Config().get('monospace_docstrings') == 'True')
        except: monospace = False
        # doc links don't work inside markdown pre/code blocks
        s = f'```\n{s}\n```' if monospace else add_doc_links(s, elt)
        doc += s
    if len(args) > 0: doc += f'\n\n{_format_args(elt)}'
    if disp: display(Markdown(doc))
    else: return doc

# Cell
def doc(
    elt, # Some function or class to pull up the documentation for
):
    "Show `show_doc` info in preview window when used in a notebook"
    md = show_doc(elt, disp=False)
    doc_link = get_doc_link(elt)
    if doc_link is not None:
        md += f'\n\n<a href="{doc_link}" target="_blank" rel="noreferrer noopener">Show in docs</a>'
    output = md2html(md)
    if IN_COLAB: get_ipython().run_cell_magic(u'html', u'', output)
    else:
        try: page.page({'text/html': output})
        except: display(Markdown(md))