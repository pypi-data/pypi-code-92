import samna
from samna.speck2b.configuration import SpeckConfiguration
from .dynapcnn import DynapcnnConfigBuilder


# Since most of the configuration is identical to DYNAP-CNN, we can simply inherit this class

class Speck2BConfigBuilder(DynapcnnConfigBuilder):

    @classmethod
    def get_samna_module(cls):
        return samna.speck2b

    @classmethod
    def get_default_config(cls) -> SpeckConfiguration:
        return SpeckConfiguration()

    @classmethod
    def get_output_buffer(cls):
        return samna.BufferSinkNode_speck2b_event_output_event()
