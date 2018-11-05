import os


def get_filename_and_path(file_path):
    """
    To split folder path and file name from argument
    @param file_path:
    @return: file_name,folder_path
    """
    try:
        index = file_path.rindex("/")
        folder_path = file_path[0:index]
        file_name = file_path[index:]
        return file_name,folder_path
    except BaseException as e:
        print("Exception in get_filename_and_path function")
        print(str(e))


def verify_arguments(argv):
    """
    Verifies command line arguments count and directories
    Verifies source and target file paths and creates output directory if not exist
    @param argv: Arguments list
    @return: boolean true or false. True when arguments are valid otherwise False
    """
    try:
        arguments_count = len(argv)
        if arguments_count == 3:  # To verify number of command line arguments
            if argv[1] == argv[2]:  # To verify source and target file paths
                print("Input and output files are same. Please check file name(s) and Path")
                return False
            else:
                input_file_name, input_folder_path = get_filename_and_path(argv[1])
                output_file_name, output_folder_path = get_filename_and_path(argv[2])
                if input_file_name and output_file_name:  # To verify file names are not empty
                    if not os.path.exists(output_folder_path):
                        print("Creating output directory")
                        os.mkdir(output_folder_path)      # Create output directory if not exist
                    return True
                else:
                    print("Invalid File Names")
                    return False
        else:
            print("Invalid Number of Arguments")
            return False
    except BaseException  as e:
        print("Exception in verify_arguments function")
        print(str(e))
        return False