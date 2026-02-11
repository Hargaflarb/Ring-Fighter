import pygame

class SoundManager():
    #singleton code; creates a new instance if none exist, otherwise returns the instance
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance=super().__new__(cls)
        return cls.instance
    #code below needs no change to work with singleton
    def __init__(self):
        self._sound_effects={}
        self._music={}
        self._current_music=None

    def Add_sfx(self,sfx_name,volume):
        sfx=pygame.mixer.Sound(f"assets\\{sfx_name}")
        sfx.set_volume(volume)
        self._sound_effects[sfx_name]=sfx

    def Add_music(self,music_name,volume):
        self._music[music_name]=volume

    def Play_sfx(self,sfx_name):
        active_sfx=self._sound_effects[sfx_name]
        active_sfx.play()


    def Play_music(self,music_name):
        pygame.mixer.music.load((f"assets\\{music_name}"))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(self._music[music_name])

    def Stop_music(self):
        pygame.mixer.music.stop()

class Sound():
    #most fields should not be editable after the class is initialised
    def __init__(self,name,sound,volume):
        self._sound_name=name
        self._sound=sound
        self._volume=volume
    
    @property
    def name(self):
        return self._sound_name
    
    @property
    def sound(self):
        return self._sound
    
    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self,value):
        self._volume=value

    