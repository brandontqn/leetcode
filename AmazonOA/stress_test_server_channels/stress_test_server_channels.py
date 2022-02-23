def getMedian(packets):
    n = len(packets)
    if n % 2 == 0:
        return (packets[n//2 - 1] + packets[n//2]) / 2
    else:
        return packets[n//2]

def maxSumQualities(packets, channels):
    sorted_packets = sorted(packets)
    channel_idx = channels
    res = 0
    while channel_idx > 1:
        res += sorted_packets.pop()
        channel_idx -= 1

    res += getMedian(sorted_packets[:len(sorted_packets) - channels + 2])
    return res

def main():
    packets = [1, 2, 3, 4, 5]
    channels = 2
    result = maxSumQualities(packets, channels)
    print(result)

if __name__ == "__main__":
    main()