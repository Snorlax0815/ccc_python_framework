import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
from markus import CCC
class Loader:
    """
    This class will read the desired input file, parse it for desired data
    using the function given as a parameter for the run_case method,
    and then launch the appropriate function.
    This class will also be responsible for writing the output to the desired
    output file.
    Author: Markus Rafeiner
    Version: 1.1
    """
    def run_case(self, level, case, parser, executor):
        """
        This method will read the input file,
        parse it using the parser function,
        and then execute the executor function.
        The result os saved in the appropriate output file.
        :param level: the level of the input file. >=1
        :param case: the case number of the input file. >=1
        :param parser: the method that will parse the input file. returns a list of the desired data, each entry is a case.
        :param executor: the method that will execute the desired function. returns a list of the result of each case.
        """
        input_path = f"source_files/level{level}/level{level}-{case}.in"
        output_path = f"output_files/level{level}/level{level}-{case}.out"

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Now open the files
        with open(input_path, "r") as file, open(output_path, "w+") as output:
            parsed_data = parser(file)
            return_data = executor(parsed_data)
            print(return_data)

    def run_all_cases(self,level, parser, executor):
        """
        This method will read all input files of the given level,
        parse them using the parser function,
        and then execute the executor function.
        The result os saved in the appropriate output files.
        :param level: the level of the input file. >=1
        :param parser: the method that will parse the input file. returns a list of the desired data, each entry is a case.
        :param executor: the method that will execute the desired function. returns a list of the result of each case.
        """
        input_dir = f"source_files/level{level}/"
        output_dir = f"output_files/level{level}/"

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_dir), exist_ok=True)

        # Now open the files
        for file in os.listdir(input_dir):
            if os.path.isfile(input_dir + file) and file.endswith(".in"):
                with open(input_dir+file, "r") as file, open(file.name.replace(".in", ".out")
                                                                     .replace("source", "output"), "w+") as output:
                    print(f"\n\n\n\n\nread file name {file.name}")
                    parsed_data = parser(file)
                    return_data = executor(parsed_data)
                    print(return_data, file = output)

    def run_example(self, parser, executor):
        """
        This method will read the example input file,
        parse it using the parser function,
        and then execute the executor function.
        The result os saved in the appropriate output file.
        :param parser: the method that will parse the input file. returns a list of the desired data, each entry is a case.
        :param executor: the method that will execute the desired function. returns a list of the result of each case.
        """
        input_path = f"source_files/level1/level1_example.in"
        output_path = f"output_files/level1/level1_example.out"

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Now open the files
        with open(input_path, "r") as file, open(output_path, "w+") as output:
            parsed_data = parser(file)
            return_data = executor(parsed_data)
            print(return_data, file = output)


if __name__ == '__main__':
    loader = Loader()
    CCC = CCC()
    parser = CCC.lvl3_parser
    executor = CCC.lvl3_executor
    # loader.run_case(3, 3, parser, executor)
    loader.run_all_cases(3, parser, executor)
    # loader.run_example(parser, executor)
