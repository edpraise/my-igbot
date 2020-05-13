from instapy import InstaPy

session = InstaPy(username="iamedpraize", password = "hellomum22")
session.login()
session.like_by_tags(["shredwars", "F-35", "speed","hillsong united"], amount=5)
session.set_dont_like(["naked", "nude", "boobs"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["cool", "dope","sick"])
session.end()

session.set_quota_supervisor(enabled=True, peak_comments_daily=20, peak_comments_hourly=21)
session = InstaPy(username='iamedpraize', password='hellomum22', headless_browser=True)

session.set_relationship_bounds(enabled=True, max_followers=1000)





