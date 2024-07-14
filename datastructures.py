from typing import Optional, List
from markupsafe import Markup

class Image:
    def __init__(self, url: str, layout: Optional[str] = None, caption: Optional[str] = None):
        self.url = url
        self.layout = layout
        self.caption = caption

class SubSection:
    def __init__(self, type: str, heading: str, content: Markup, images: Optional[List[Image]] = None):
        self.type = type
        self.heading = heading
        self.content = content
        self.images = images

class Section:
    def __init__(self, sub_sections: List[SubSection], heading: Optional[str] = None):
        self.heading = heading
        self.sub_sections = sub_sections

class Label:
    def __init__(self, name: str):
        self.name = name

class Meta:
    def __init__(self, client: str, role: str, duration: str, location: str):
        self.client = client
        self.role = role
        self.duration = duration
        self.location = location

class CaseStudy:
    def __init__(self, id: int, name: str, description: str, lead: str, hero_img_url: str, hero_img_raw_url: str, labels: List[Label], meta: Meta, sections: List[Section]):
        self.id = id
        self.name = name
        self.description = description
        self.lead = lead
        self.hero_img_url = hero_img_url
        self.hero_img_raw_url = hero_img_raw_url
        self.labels = labels
        self.meta = meta
        self.sections = sections