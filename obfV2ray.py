import base64
import json
import argparse

def add_obfuscation(config, network, path, headers, security, tls_settings, socks_settings):
    # Load the V2ray config as a Python dictionary
    config_dict = json.loads(config)

    # Add the obfuscation settings to the config
    config_dict["outbounds"][0]["streamSettings"] = {
        "network": network,
        "wsSettings": {
            "path": path,
            "headers": headers
        },
        "security": security,
        "tlsSettings": tls_settings,
        "socksSettings": socks_settings
    }

    # Convert the modified config back to a JSON string
    modified_config = json.dumps(config_dict, indent=2)

    return modified_config

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Add obfuscation to a V2ray config file")
    parser.add_argument("input_file", help="Path to the input V2ray config file")
    parser.add_argument("output_file", help="Path to the output V2ray config file")
    parser.add_argument("--network", default="ws", help="Network protocol (default: ws)")
    parser.add_argument("--path", default="/", help="WebSocket path (default: /)")
    parser.add_argument("--headers", default='{"Host": "example.com"}', help="WebSocket headers (default: {'Host': 'example.com'})")
    parser.add_argument("--security", default="tls", help="Security protocol (default: tls)")
    parser.add_argument("--tls-settings", default='{"allowInsecure": true, "serverName": "example.com"}', help="TLS settings (default: {'allowInsecure': true, 'serverName': 'example.com'})")
    parser.add_argument("--socks-settings", default='{"auth": "password", "accounts": [{"user": "username", "pass": "cGFzc3dvcmQ="}]}', help="SOCKS settings (default: {'auth': 'password', 'accounts': [{'user': 'username', 'pass': 'cGFzc3dvcmQ='}]})")
    args = parser.parse_args()

    # Read the input V2ray config file
    with open(args.input_file, "r") as f:
        config = f.read()

    # Add obfuscation to the config
    headers = json.loads(args.headers)
    tls_settings = json.loads(args.tls_settings)
    socks_settings = json.loads(args.socks_settings)
    modified_config = add_obfuscation(config, args.network, args.path, headers, args.security, tls_settings, socks_settings)

    # Write the modified config to the output file
    with open(args.output_file, "w") as f:
        f.write(modified_config)
