def codeBlocksToText(chunks):
    result = ""
    for chunk in chunks:
        for code in chunk:
            result += chr(code)
    return result


def textToCodeBlocks(text: str, chunkSize: int, filler: int):
    text = text.encode()
    result = []
    l = len(text)
    for i in range(0, l, chunkSize):
        chunk = []
        for j in range(i, min(l, i + chunkSize), 1):
            chunk.append(text[j])
        if len(chunk) < chunkSize:
            chunk.extend([filler] * (chunkSize - len(chunk)))
        result.append(chunk)
    return result

