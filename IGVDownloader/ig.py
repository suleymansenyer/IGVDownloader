import instaloader

L = instaloader.Instaloader()

def ig_get_pp(username:str):
    profile = instaloader.Profile.from_username(L.context,username)
    return profile.profile_pic_url
    

def video_get_source(shortcode:str):
    post = instaloader.Post.from_shortcode(L.context,shortcode=shortcode)
    return post.video_url

