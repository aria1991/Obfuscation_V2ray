# Obfuscation_V2ray
Adding obfuscation script in python to V2ray

- This version of the script is designed to be run from the command line, and it takes a number of optional arguments that allow you to customize the obfuscation settings.
<!--more-->


- The `input_file` and `output_file` arguments are required, and they specify the path to the input V2ray config file and the path to the output V2ray config file, respectively.
<!--more-->


- The remaining arguments are optional and allow you to customize the obfuscation settings. The default values are provided in the argument definitions.
<!--more-->


- The script reads the input V2ray config file, adds the specified obfuscation settings using the `add_obfuscation` function, and then writes the modified config to the output file.
