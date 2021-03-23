import lagan


def main():
    case1()
    # case2()
    # case3()
    # case4()


def case1():
    lagan.load()
    lagan.set_filter_level(lagan.LEVEL_DEBUG)
    lagan.enable_color(False)
    lagan.println('case1', lagan.LEVEL_OFF, 'TestPrintOut1:%d', 100)
    lagan.println('case1', lagan.LEVEL_DEBUG, 'TestPrintOut1:%d', 100)
    lagan.println('case1', lagan.LEVEL_INFO, 'TestPrintOut1:%d', 100)
    lagan.println('case1', lagan.LEVEL_WARN, 'TestPrintOut1:%d', 100)
    lagan.println('case1', lagan.LEVEL_ERROR, 'TestPrintOut1:%d', 100)

    s = bytearray()
    for i in range(100):
        s.append(i)
    lagan.print_hex('case1', lagan.LEVEL_INFO, s)


def case2():
    lagan.load()
    s = bytearray()
    for i in range(100):
        s.append(i)
    lagan.print_hex('case2', lagan.LEVEL_ERROR, s)


def case3():
    lagan.load()
    lagan.debug('case3', 'print:%d,a=%d', 101, 102)
    lagan.warn('case3', 'print:%d,b=%d', 101, 102)


def case4():
    # 日志模块载入.全局载入一次,参数是分割文件大小,默认是10M
    lagan.load()

    # 默认输出界别是info,本行不会打印
    lagan.debug("case4", "debug test print")

    lagan.info("case4", "info test print")
    lagan.warn("case4", "warn test print")
    lagan.error("case4", "error test print")


if __name__ == '__main__':
    main()
