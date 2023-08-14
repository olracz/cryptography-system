import secrets


def generate_and_store_keys(env_file_path='.env', levels_to_generate=None):
    # Caesar shift, prefix, and suffix are only generated for level 1
    if levels_to_generate is None:
        levels_to_generate = [1, 2, 3, 4, 5]
    caesar_shift = secrets.randbelow(256)  # Generates a random integer from 0 to 256
    prefix = secrets.token_hex(16)
    suffix = secrets.token_hex(16)

    # Read the existing content of the .env file and remove lines for specified keys and levels
    with open(env_file_path, 'r') as env_file:
        lines = env_file.readlines()

    lines = [line for line in lines if
             not any(line.startswith(f'XOR_KEY_LEVEL{level}=') for level in levels_to_generate) and
             not line.startswith('CAESAR_SHIFT=') and
             not line.startswith('PREFIX=') and
             not line.startswith('SUFFIX=')]

    # Write the updated content back to the .env file
    with open(env_file_path, 'w') as env_file:
        env_file.writelines(lines)

    # Generate new XOR keys for levels 1 to 5 and write them to the .env file
    for level in levels_to_generate:
        new_xor_key = secrets.token_hex(16)
        with open(env_file_path, 'a') as env_file:
            env_file.write(f'XOR_KEY_LEVEL{level}={new_xor_key}\n')

    # Write Caesar shift, prefix, and suffix values for level 1 to the .env file
    with open(env_file_path, 'a') as env_file:
        env_file.write(f'CAESAR_SHIFT={caesar_shift}\n')
        env_file.write(f'PREFIX={prefix}\n')
        env_file.write(f'SUFFIX={suffix}\n')

    print("New XOR keys, Caesar shift, prefix, and suffix generated and stored in .env file.")


if __name__ == "__main__":
    generate_and_store_keys()
