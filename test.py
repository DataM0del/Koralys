import unittest
from koralys import deserialize_v5, deserialize_v6, decompile, read_constant, read_proto_data, create_empty_proto
from reader import Reader

class TestKoralys(unittest.TestCase):

    def test_deserialize_v5(self):
        with open("compile/output_v5.luac", "rb") as f:
            bytecode = f.read()
        reader = Reader(bytecode)
        reader.skip(1) # skip bytecode version
        result = deserialize_v5(reader)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 5)

    def test_deserialize_v6(self):
        with open("compile/output_v6.luac", "rb") as f:
            bytecode = f.read()
        reader = Reader(bytecode)
        reader.skip(1) # skip bytecode version
        result = deserialize_v6(reader)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 5)

    def test_decompile(self):
        with open("compile/output_v5.luac", "rb") as f:
            bytecode = f.read()
        reader = Reader(bytecode)
        reader.skip(1) # skip bytecode version
        main_proto, proto_table, string_table, luau_version, types_version = deserialize_v5(reader)
        output = decompile(main_proto, 1, string_table, luau_version)
        self.assertIn("local function func1", output)

if __name__ == '__main__':
    unittest.main()
