def writeText(text):
    # if __name__ == '__main__':
    queue.append(text)
    for c in queue:
        time.sleep(0.5)
        PressKey(c)
        time.sleep(0.5)
        ReleaseKey(c)

writeText("Titan's treasure")
