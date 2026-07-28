# Plan: Replace profile image with ASCII art in dark.svg and light.svg

## Global Constraints
- The ASCII art must be generated from the current profile.jpg (the same one used in the SVG).
- The ASCII art must fit within the existing avatar clip region (x="42" y="88" width="470" height="286").
- Use a monospace font and appropriate font size to fit the art.
- For dark.svg, use light text color (#d8e5ff). For light.svg, use dark text color (#0f172a).
- Preserve the existing clip-path (id="avatarClip") for the ASCII art.

## Tasks

1. Generate ASCII art from profile.jpg with width 45 (or appropriate) and save ascii.txt.
2. Update dark.svg: replace the <image> element with a <text> element containing the ASCII art from ascii.txt.
3. Update light.svg: similarly replace the <image> element with a <text> element containing the ASCII art.