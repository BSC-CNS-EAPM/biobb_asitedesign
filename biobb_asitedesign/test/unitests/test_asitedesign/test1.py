from biobb_asitedesign.asitedesign.asitedesign_container import asitedesign_container


def main():
    prop = {
        "threads": 2,
        "database": ".",
        "binary_path": ".",
        'support_folder': ".",
        "remove_tmp": False
    }

    rcode = asitedesign_container(input_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/test.fasta",
                    output_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/output.zip",
                    properties=prop)


if __name__ == '__main__':
    main()