# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_google_native.gkehub.v1 as v1
    import pulumi_google_native.gkehub.v1alpha as v1alpha
    import pulumi_google_native.gkehub.v1alpha2 as v1alpha2
    import pulumi_google_native.gkehub.v1beta as v1beta
    import pulumi_google_native.gkehub.v1beta1 as v1beta1
else:
    v1 = _utilities.lazy_import('pulumi_google_native.gkehub.v1')
    v1alpha = _utilities.lazy_import('pulumi_google_native.gkehub.v1alpha')
    v1alpha2 = _utilities.lazy_import('pulumi_google_native.gkehub.v1alpha2')
    v1beta = _utilities.lazy_import('pulumi_google_native.gkehub.v1beta')
    v1beta1 = _utilities.lazy_import('pulumi_google_native.gkehub.v1beta1')

