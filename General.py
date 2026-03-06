class CircularRotation:#循环移位工具类

    @staticmethod
    def left(value,shift,width=32):
        shift=shift%width
        mask=(1<<width)-1
        return ((value<<shift)|(value>>(width-shift)))&mask

    @staticmethod
    def right(value,shift,width=32):
        shift=shift%width
        mask=(1<<width)-1
        return ((value>>shift)|(value<<(width-shift)))&mask
