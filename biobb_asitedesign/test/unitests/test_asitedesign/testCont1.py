from biobb_asitedesign.asitedesign.asitedesign_container import asitedesign_container


def main():
    prop = {
        "threads": 2,
        "database": ".",
        "remove_tmp": False,
        "container_image": "bsceapm/asitedesign:1.9"
    }

    rcode = asitedesign_container(
        input_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/test.fasta",
        output_path="/home/albertcs/GitHub/EAPM/biobb_ahatool/biobb_ahatool/test/data/ahatool/output.zip",
        properties=prop)


if __name__ == '__main__':
    main()
