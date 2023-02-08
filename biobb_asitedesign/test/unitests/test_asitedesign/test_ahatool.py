from biobb_common.tools import test_fixtures as fx
from biobb_asitedesign.asitedesign.asitedesign import asitedesign

class TestAsitedesign():
    def setup_class(self):
        fx.test_setup(self, 'asitedesing')

    def teardown_class(self):
        fx.test_teardown(self)
        pass
    def test_ahatool(self):
        returncode= asitedesign(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_file_path'])
        assert fx.equal(self.paths['output_file_path'], self.paths['ref_output_file_path'])
        assert fx.exe_success(returncode)
