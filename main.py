# This is a sample Python script.
from PIL import Image, ImageFont, ImageDraw
import pprint

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def find_background():
    import cssutils
    theme = open("/usr/share/gnome-shell/theme/Yaru/gnome-shell-theme.gresource", "r")

    dct = {}
    sheet = cssutils.parseString(theme.read())

    for rule in sheet:
        selector = rule.selectorText
        styles = rule.style.cssText
        dct[selector] = styles


def find_system_stats():
    import platform, psutil
    system = {
        'os': get_os(),
        'nodename': platform.node(),
        'interfaces': get_interfaces(),
        'cpu': get_cpus(),
        'memory': get_memory(),
        'storage': get_storage(),
        'uptime': get_uptime(),
        'kernel': get_kernel()
        }
    return system


def get_cores():
    import os
    return os.cpu_count()


def get_cpus():
    cores = get_cores()
    return cores


def get_dns():
    return 0


def netmask_to_cidr(m_netmask):
    bitmask = sum([bin(int(bits)).count("1") for bits in m_netmask.split(".")])
    return str(bitmask)


def get_interfaces():
    network = {}
    ifdict = []
    from netifaces import interfaces, ifaddresses, AF_INET, gateways
    for ifaceName in interfaces():
        if 2 in ifaddresses(ifaceName).keys():
            ipv4 = ifaddresses(ifaceName)[2][0]
            addr = ipv4['addr'] + "/" + netmask_to_cidr(ipv4['netmask'])
            case = {'ifaceName': ifaceName, 'inet': addr}
            ifdict.append(case)
    get_dns()
    network = {'routes': gateways(), 'interfaces': ifdict, 'dns': get_dns() }
    return network


def get_kernel():
    return 0


def get_memory():
    import psutil
    return psutil.virtual_memory()[0]


def get_os():
    with open('/etc/os-release', 'r') as f:
        uptime_seconds = f
    return 0


def get_routing(gwlist):
    gws = gwlist()
    return gws


def get_storage():
    return 0


def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds


def modify_file(name):
    my_image = Image.open("test_files/Jammy-Jellyfish_WP_4096x2304_Grey.png")
    title_font = ImageFont.truetype('test_files/LiberationMono-Bold.ttf', 200)
    title_text = name
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((15, 15), title_text, (237, 230, 211), font=title_font)
    my_image.save("result.png")


def main():
    import json
    stats = find_system_stats()
    print(json.dumps(stats, sort_keys=False, indent=4))
    modify_file('PyCharm')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
