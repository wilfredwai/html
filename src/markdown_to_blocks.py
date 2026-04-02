def markdown_to_blocks(markdown):
    output = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            stripped_line = []
            lines = block.split("\n")
            for line in lines:
                stripped_line.append(line.strip())
            stripped = "\n".join(stripped_line)
            stripped = stripped.strip()
            if stripped:
                output.append(stripped)
    return output
