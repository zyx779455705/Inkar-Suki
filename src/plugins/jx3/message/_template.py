template_chat_records_head = """
<th class="record-index">序号</th>
<th class="record-time">时间</th>
<th class="record-channel">频道</th>
<th class="record-message">发言内容</th>
"""

template_chat_record = """
<tr>
    <td class="record-index">{{ index }}</td>
    <td class="record-time">{{ time }}</td>
    <td class="record-channel"><span class="channel-tag">{{ channel }}</span></td>
    <td class="record-message">{{ message }}</td>
</tr>
"""

chat_records_css = """
.container {
    width: 1280px;
    min-width: 0;
    box-sizing: border-box;
}

.item-table {
    width: 100%;
    min-width: 0;
    table-layout: fixed;
}

.item-table th,
.item-table td {
    box-sizing: border-box;
}

.item-table .record-index {
    width: 80px;
}

.item-table .record-time {
    width: 230px;
    color: #7f8c8d;
}

.item-table .record-channel {
    width: 130px;
}

.item-table .record-message {
    width: 760px;
    text-align: left;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    word-break: break-word;
    line-height: 1.55;
}

.channel-tag {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 12px;
    background: #e8f4ff;
    color: #2c7be5;
    white-space: nowrap;
}
"""
