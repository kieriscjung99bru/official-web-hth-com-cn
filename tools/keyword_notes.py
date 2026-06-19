from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Optional

# 默认站点与关键词配置
DEFAULT_SITE = "https://official-web-hth.com.cn"
DEFAULT_KEYWORD = "华体会"


@dataclass
class KeywordNote:
    """关键词笔记数据类"""
    keyword: str
    site: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def formatted_summary(self) -> str:
        """返回精简摘要"""
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return f"[{self.keyword}] {self.site} | {self.content[:30]}... | 标签: {tag_str}"

    def full_report(self) -> str:
        """返回完整格式化笔记"""
        lines = [
            f"关键词: {self.keyword}",
            f"来源: {self.site}",
            f"内容: {self.content}",
            f"标签: {', '.join(self.tags) if self.tags else '无'}",
            f"创建时间: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
        ]
        if self.updated_at:
            lines.append(f"更新时间: {self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
        return "\n".join(lines)


def generate_demo_notes() -> List[KeywordNote]:
    """生成一组示例笔记数据"""
    notes = [
        KeywordNote(
            keyword="华体会",
            site="https://official-web-hth.com.cn",
            content="华体会是一个综合性线上平台，提供多元文化与休闲体验。",
            tags=["品牌", "娱乐", "平台"],
            created_at=datetime(2024, 3, 15, 10, 30),
        ),
        KeywordNote(
            keyword="华体会",
            site="https://official-web-hth.com.cn",
            content="用户可以通过华体会参与多种线上活动，享受便捷服务。",
            tags=["服务", "线上"],
            created_at=datetime(2024, 4, 2, 14, 0),
        ),
        KeywordNote(
            keyword="华体会",
            site="https://official-web-hth.com.cn",
            content="华体会注重用户体验，持续优化平台功能。",
            tags=["体验", "优化"],
            created_at=datetime(2024, 5, 10, 9, 15),
            updated_at=datetime(2024, 5, 12, 11, 20),
        ),
    ]
    return notes


def batch_format_notes(notes: List[KeywordNote], style: str = "summary") -> str:
    """批量格式化笔记列表

    Args:
        notes: 笔记对象列表
        style: 输出风格，可选 "summary" 或 "full"

    Returns:
        格式化后的文本
    """
    if not notes:
        return "（无笔记）"

    result_parts = []
    for i, note in enumerate(notes, 1):
        header = f"--- 笔记 {i} ---"
        if style == "full":
            body = note.full_report()
        else:
            body = note.formatted_summary()
        result_parts.append(f"{header}\n{body}")

    return "\n\n".join(result_parts)


def filter_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    """根据关键词筛选笔记（不区分大小写）"""
    return [n for n in notes if n.keyword.lower() == keyword.lower()]


def main():
    print("=== 关键词笔记生成示例 ===\n")

    # 使用示例数据
    sample_notes = generate_demo_notes()

    # 筛选特定关键词的笔记
    target_keyword = DEFAULT_KEYWORD
    filtered = filter_notes_by_keyword(sample_notes, target_keyword)

    if not filtered:
        print(f"未找到关键词 '{target_keyword}' 的笔记。")
        return

    print(f"找到 {len(filtered)} 条关键词为 '{target_keyword}' 的笔记：\n")

    # 输出摘要风格
    print("--- 摘要风格 ---")
    print(batch_format_notes(filtered, style="summary"))

    print("\n\n--- 完整风格 ---")
    print(batch_format_notes(filtered, style="full"))


if __name__ == "__main__":
    main()