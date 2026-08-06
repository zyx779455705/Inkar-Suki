table_head = """
<tr>
    <th class="short-column">排行</th>
    <th class="short-column">头像</th>
    <th class="short-column">昵称</th>
    <th class="short-column">QQ号</th>
    <th class="short-column">发言</th>
</tr>"""

template_body = """
<tr>
    <td class="short-column">{{ rank }}</td>
    <td class="short-column"><img src="{{ avatar }}" alt="icon" width="30" height="30"></td>
    <td class="short-column">{{ nickname }}</td>
    <td class="short-column">{{ user_id }}</td>
    <td class="short-column">{{ count }}</td>
</tr>
"""

command_summary_head = """
<th class="stats-rank-column">排行</th>
<th class="stats-key-column">命令</th>
<th>总调用</th>
<th>今日</th>
<th>近 7 日</th>
<th class="stats-time-column">最近调用</th>
"""

command_detail_head = """
<th>统计项</th>
<th>数值</th>
<th>补充信息</th>
<th>趋势 / 间隔</th>
"""

command_statistics_css = """
.container {
    min-width: 1180px;
}

.item-table {
    min-width: 1180px;
}

.stats-rank-column {
    width: 90px;
}

.stats-key-column {
    min-width: 220px;
    font-weight: 600;
    color: #2c3e50;
}

.stats-time-column {
    min-width: 260px;
}

.stats-zero {
    color: #a0a0a0;
}

.stats-section td {
    padding: 10px 18px;
    text-align: left;
    background: #f1f5f9;
    color: #334155;
    font-weight: 600;
}

.stats-card-row td {
    padding: 18px;
    background: #fff;
}

.stats-cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
}

.stats-card {
    padding: 16px 12px;
    border-radius: 8px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
}

.stats-card-label {
    color: #64748b;
    font-size: 19px;
}

.stats-card-value {
    margin-top: 5px;
    color: #1e293b;
    font-size: 30px;
    font-weight: 700;
}

.stats-meta {
    margin-top: 14px;
    color: #64748b;
    font-size: 19px;
    text-align: left;
}

.stats-bar-track {
    display: inline-block;
    width: 220px;
    height: 14px;
    overflow: hidden;
    vertical-align: middle;
    border-radius: 7px;
    background: #e2e8f0;
}

.stats-bar {
    height: 100%;
    border-radius: 7px;
    background: #76c7c0;
}

.stats-up {
    color: #16a34a;
}

.stats-down {
    color: #dc2626;
}

.stats-muted {
    color: #94a3b8;
}

.stats-message {
    padding: 34px !important;
    color: #475569;
    white-space: normal !important;
}
"""
