# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_google_native.cloudbuild.v1 as v1
    import pulumi_google_native.cloudbuild.v1alpha1 as v1alpha1
    import pulumi_google_native.cloudbuild.v1alpha2 as v1alpha2
    import pulumi_google_native.cloudbuild.v1beta1 as v1beta1
else:
    v1 = _utilities.lazy_import('pulumi_google_native.cloudbuild.v1')
    v1alpha1 = _utilities.lazy_import('pulumi_google_native.cloudbuild.v1alpha1')
    v1alpha2 = _utilities.lazy_import('pulumi_google_native.cloudbuild.v1alpha2')
    v1beta1 = _utilities.lazy_import('pulumi_google_native.cloudbuild.v1beta1')

