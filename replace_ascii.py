import xml.etree.ElementTree as ET
import sys

def replace_image_with_ascii(svg_file, ascii_file, output_file, fill_color):
    # Parse the SVG
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Namespace for SVG and xlink
    ns = {'svg': 'http://www.w3.org/2000/svg', 'xlink': 'http://www.w3.org/1999/xlink'}
    ET.register_namespace('', ns['svg'])
    ET.register_namespace('xlink', ns['xlink'])

    # Find the image element with the specific attributes
    # We'll search for any image element with x="42", y="88", width="470", height="286"
    for elem in root.iter():
        if elem.tag.endswith('}image'):
            x = elem.get('x')
            y = elem.get('y')
            width = elem.get('width')
            height = elem.get('height')
            if x == '42' and y == '88' and width == '470' and height == '286':
                # Found the image element to replace
                parent = None
                for p in root.iter():
                    for child in p:
                        if child == elem:
                            parent = p
                            break
                    if parent:
                        break

                if parent is not None:
                    # Remove the image element
                    parent.remove(elem)

                    # Create a text element
                    text_elem = ET.Element('text')
                    text_elem.set('x', '42')
                    text_elem.set('y', '88')
                    text_elem.set('fill', fill_color)
                    text_elem.set('font-family', 'ui-monospace, Menlo, Consolas, monospace')
                    text_elem.set('font-size', '8')
                    # Set the clip-path to match the original
                    text_elem.set('clip-path', 'url(#avatarClip)')

                    # Read ASCII art lines
                    with open(ascii_file, 'r') as f:
                        lines = [line.rstrip('\n') for f in [f] for line in f]  # This is a bit ugly, let's fix
                    # Actually, let's do it properly:
                    with open(ascii_file, 'r') as f:
                        lines = [line.rstrip('\n') for line in f]

                    # Add each line as a tspan
                    for i, line in enumerate(lines):
                        tspan = ET.Element('tspan')
                        tspan.set('x', '42')
                        if i > 0:
                            tspan.set('dy', '1.2em')
                        tspan.text = line
                        text_elem.append(tspan)

                    # Insert the text element where the image was
                    parent.append(text_elem)
                break

    # Write the modified SVG
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python replace_ascii.py <svg_file> <ascii_file> <output_file> <fill_color>")
        sys.exit(1)
    svg_file = sys.argv[1]
    ascii_file = sys.argv[2]
    output_file = sys.argv[3]
    fill_color = sys.argv[4]
    replace_image_with_ascii(svg_file, ascii_file, output_file, fill_color)
    print(f"Replaced image in {svg_file} with ASCII art, saved to {output_file}")