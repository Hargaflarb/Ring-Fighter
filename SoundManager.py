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
        #self._current_music=None
        self._music_volume=1
        self._sfx_volume=1
        print("i got initiated")
    
    def Add_sfx(self,sfx_name,sfx_file,volume):
        #!make sure the asset is in the correct sub-folder!
        sfx=pygame.mixer.Sound(f"assets\\Audio\\{sfx_file}")
        sfx.set_volume(volume)
        self._sound_effects[sfx_name]=sfx

    def Add_music(self,music_name,music_file,volume):
        self._music[music_name]=Audio(music_file,volume)

    def Play_sfx(self,sfx_name):
        active_sfx=self._sound_effects[sfx_name]
        active_sfx.play()

    def Write_sound_effects(self):
        print("sound effects are:")
        for sound in self._sound_effects.keys():
            print(sound, end = ", ")


    def Play_music(self,music_name):
        #!make sure the asset is in the correct sub-folder!
        pygame.mixer.music.load((f"assets\\Audio\\{self._music[music_name].file_name}"))
        pygame.mixer.music.play(-1)
        self._current_music=self._music[music_name]
        pygame.mixer.music.set_volume(self._music[music_name].volume*self._music_volume)

    def Stop_music(self):
        pygame.mixer.music.stop()

    def Change_music_volume(self,value):
        self._music_volume=value
        pygame.mixer.music.set_volume(self._current_music.volume*value)

    def Change_sfx_volume(self,value):
        for key,sound in self._sound_effects:
            sound.volume=sound.volume/self._sfx_volume
        self._sfx_volume=value
        for key,sound in self._sound_effects:
            sound.volume=sound.volume*self._sfx_volume

class Audio():
    #most fields should not be editable after the class is initialised
    def __init__(self,file_name,volume):
        self._file_name=file_name
        self._volume=volume
    
    @property
    def file_name(self):
        return self._file_name
    
    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self,value):
        self._volume=value

    