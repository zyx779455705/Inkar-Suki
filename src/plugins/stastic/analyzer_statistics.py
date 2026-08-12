from nonebot.adapters.onebot.v11 import MessageSegment

from src.utils.analyzer_usage import get_analyzer_prefixes

from .command_statistics import UsageStatisticsConfig, render_usage_statistics


ANALYZER_STATISTICS_CONFIG = UsageStatisticsConfig(
    table_name="analyzer_usage",
    key_column="prefix",
    title="分析器统计",
    key_heading="前缀",
    key_noun="前缀",
    query_noun="分析器前缀",
    action="使用",
)


async def render_analyzer_statistics(prefix_query: str = "") -> MessageSegment:
    return await render_usage_statistics(
        ANALYZER_STATISTICS_CONFIG,
        get_analyzer_prefixes(),
        prefix_query,
    )
