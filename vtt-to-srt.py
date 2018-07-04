import sys, webvtt
from pysrt import SubRipFile, SubRipItem


def main():
	vtt , srt , index = webvtt.read(sys.argv[1]) , SubRipFile() , 0
	for block in vtt:
		srt.append(SubRipItem(index, start=block.start, end=block.end, text=block.text))
		index += 1
	srt.save(sys.argv[1].split('.')[0] +".srt", encoding="utf8")
	exit(0)


if __name__ == '__main__':
	main()
