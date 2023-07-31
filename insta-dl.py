import instaloader

def download_reel(username):
    try:
        loader = instaloader.Instaloader()

        # Load the profile of the user
        profile = instaloader.Profile.from_username(loader.context, username)

        # Retrieve the reels of the user
        reels = profile.get_posts()

        # Download the reels
        for reel in reels:
            if reel.is_video:
                loader.download_post(post=reel, target=profile.username)

        print("done")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"[e] '{username}' not found.")
    except Exception as e:
        print(f"[e] {e}")