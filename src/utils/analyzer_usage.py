from collections.abc import Iterable

from nonebot.log import logger

from src.utils.database import logs_db
from src.utils.database.classes import AnalyzerUsage
from src.utils.time import Time


ANALYZER_PREFIXES: set[str] = set()


def register_analyzer_prefixes(prefixes: Iterable[str]) -> None:
    """注册当前进程内可参与统计的分析器前缀。"""
    ANALYZER_PREFIXES.update(prefixes)


def get_analyzer_prefixes() -> set[str]:
    """返回当前进程内所有参与统计的分析器前缀。"""
    return ANALYZER_PREFIXES.copy()


def record_analyzer_usage(prefix: str) -> None:
    """记录一次分析器前缀的使用。"""
    ANALYZER_PREFIXES.add(prefix)
    try:
        logs_db.save(
            AnalyzerUsage(
                prefix=prefix,
                timestamp=Time().raw_time,
            )
        )
    except Exception:
        logger.exception(f"分析器使用统计写入失败：{prefix}")
