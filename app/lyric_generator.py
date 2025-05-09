"""
Simple lyric generator using templates for different genres and topics.
This is a fallback for when we don't have real lyrics from a model.
"""

import random

def generate_lyrics_for_topic(topic, genre):
    """Generate lyrics for a topic using a template-based approach."""
    # Convert topic to lowercase for easier text matching
    topic_lower = topic.lower()
    
    # Remove any special characters that might interfere with matching
    topic_lower = ''.join(c for c in topic_lower if c.isalnum() or c.isspace())
    
    # Start with a template-based approach using common knowledge facts
    # This is a fallback system - in a real app, we'd call an LLM
    
    # Normalize genre format
    genre_lower = genre.lower().replace("_", " ").replace("-", " ")
    
    # Generate verses and chorus based on topic and genre
    verses = generate_verses_for_topic(topic_lower, genre_lower)
    chorus = generate_chorus_for_topic(topic_lower, genre_lower)
    
    # Assemble the full lyrics
    lyrics = f"{verses[0]}\n\n{chorus}\n\n{verses[1]}\n\n{chorus}\n\n"
    
    # Add a bridge for some genres
    if genre_lower in ["hip hop", "pop", "rock"]:
        bridge = generate_bridge_for_topic(topic_lower, genre_lower)
        lyrics += f"{bridge}\n\n{chorus}\n"
    else:
        lyrics += f"{chorus}\n"
    
    return lyrics

def generate_verses_for_topic(topic, genre):
    """Generate verses for a topic using templates."""
    verses = []
    
    # First verse - introduce the topic
    if genre == "hip hop":
        verses.append(f"Yo, listen up, I'm about to drop some knowledge\nAll about {topic}, let me take you to college\nThis ain't just a song, it's education with flow\nBy the time I'm done, you'll know all you need to know")
    elif genre == "country":
        verses.append(f"Sitting on my porch just thinking 'bout {topic}\nIt ain't always easy but it's worth understanding\nLet me tell you a story about what I've learned\nTake it from someone who's been there and returned")
    else:
        verses.append(f"Let me tell you about {topic}\nIt's something worth learning, worth knowing\nOpen your mind to the knowledge I'm showing\nBy the end of this song, you'll be growing")
    
    # Second verse - more specific details
    if genre == "hip hop":
        verses.append(f"Now that you got the basics, let's go deeper\nThe facts about {topic} couldn't be neater\nPay attention to the words that I'm saying\nThis knowledge is power, no time for delaying")
    elif genre == "country":
        verses.append(f"The second thing to know about {topic}\nIs it takes some time, and a bit of logic\nLike the crops in the field needing sun and rain\nUnderstanding comes through a little joy and pain")
    else:
        verses.append(f"There's more to learn about {topic}\nThe deeper you go, the more you'll see\nIt connects to life in ways unexpected\nMake these lessons yours, get connected")
    
    return verses

def generate_chorus_for_topic(topic, genre):
    """Generate a chorus for a topic using templates."""
    
    if genre == "hip hop":
        return f"{topic.title()}, yeah, that's what I'm talking about\n{topic.title()}, let me break it down, no doubt\nLearn it, know it, show it, grow it\n{topic.title()}, that's what this song's about"
    elif genre == "country":
        return f"Oh, {topic}, it's like a country road\nSometimes rough, sometimes smooth as you go\nBut keep on driving, keep on learning\n{topic}, it's worth knowing, that's for sure"
    else:
        return f"{topic.title()}, oh {topic}\nThe more you learn, the more you'll know\n{topic.title()}, it's worth understanding\nThis knowledge will help you, help you grow"

def generate_bridge_for_topic(topic, genre):
    """Generate a bridge section for the song."""
    
    if genre == "hip hop":
        return f"Break it down now\n{topic.title()} is essential, listen to me\nThis ain't just a lesson, it's a recipe\nFor success, for progress, for knowledge divine\nTake these words, make them yours, make them shine"
    elif genre == "country":
        return f"And when the road gets tough, and the night gets long\nRemember what you learned from this simple song\n{topic.title()} ain't just words, it's wisdom true\nCarry it with you in all that you do"
    else:
        return f"And now you know, now you see\nWhat {topic} truly means to me\nCarry this knowledge wherever you go\nLet it guide you, help you grow"