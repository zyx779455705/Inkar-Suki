def read(Path):
    try:
        cache = open(Path,mode="r", encoding="utf-8")
        msg = cache.read()
        cache.close()
        return msg
    except:
        return "{}" # 默认返回空对象

def write(Path, sth):
    cache = open(Path, mode="w", encoding="utf-8")
    cache.write(sth)
    cache.close()
    return True
