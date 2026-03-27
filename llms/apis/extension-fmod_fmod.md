# extension-fmod

**Namespace:** `fmod`
**Language:** Lua
**Type:** Extension

FMOD Low Level API for audio playback and manipulation.

This module provides access to FMOD's low-level audio engine, allowing you to:
- Create and play sounds
- Control audio channels and channel groups
- Apply DSP effects
- Handle 3D audio positioning

For more information, see the [FMOD documentation](https://www.fmod.com/docs).

## API

### THREAD_TYPE_MIXER
*Type:* VARIABLE
Thread type - mixer.

### THREAD_TYPE_FEEDER
*Type:* VARIABLE
Thread type - feeder.

### THREAD_TYPE_STREAM
*Type:* VARIABLE
Thread type - stream.

### THREAD_TYPE_FILE
*Type:* VARIABLE
Thread type - file.

### THREAD_TYPE_NONBLOCKING
*Type:* VARIABLE
Thread type - nonblocking.

### THREAD_TYPE_RECORD
*Type:* VARIABLE
Thread type - record.

### THREAD_TYPE_GEOMETRY
*Type:* VARIABLE
Thread type - geometry.

### THREAD_TYPE_PROFILER
*Type:* VARIABLE
Thread type - profiler.

### THREAD_TYPE_STUDIO_UPDATE
*Type:* VARIABLE
Thread type - studio update.

### THREAD_TYPE_STUDIO_LOAD_BANK
*Type:* VARIABLE
Thread type - studio load bank.

### THREAD_TYPE_STUDIO_LOAD_SAMPLE
*Type:* VARIABLE
Thread type - studio load sample.

### THREAD_TYPE_CONVOLUTION1
*Type:* VARIABLE
Thread type - convolution1.

### THREAD_TYPE_CONVOLUTION2
*Type:* VARIABLE
Thread type - convolution2.

### OK
*Type:* VARIABLE
Operation completed successfully.

### ERR_BADCOMMAND
*Type:* VARIABLE
Error - badcommand.

### ERR_CHANNEL_ALLOC
*Type:* VARIABLE
Error - channel alloc.

### ERR_CHANNEL_STOLEN
*Type:* VARIABLE
Error - channel stolen.

### ERR_DMA
*Type:* VARIABLE
Error - dma.

### ERR_DSP_CONNECTION
*Type:* VARIABLE
Error - dsp connection.

### ERR_DSP_DONTPROCESS
*Type:* VARIABLE
Error - dsp dontprocess.

### ERR_DSP_FORMAT
*Type:* VARIABLE
Error - dsp format.

### ERR_DSP_INUSE
*Type:* VARIABLE
Error - dsp inuse.

### ERR_DSP_NOTFOUND
*Type:* VARIABLE
Error - dsp notfound.

### ERR_DSP_RESERVED
*Type:* VARIABLE
Error - dsp reserved.

### ERR_DSP_SILENCE
*Type:* VARIABLE
Error - dsp silence.

### ERR_DSP_TYPE
*Type:* VARIABLE
Error - dsp type.

### ERR_FILE_BAD
*Type:* VARIABLE
Error - file bad.

### ERR_FILE_COULDNOTSEEK
*Type:* VARIABLE
Error - file couldnotseek.

### ERR_FILE_DISKEJECTED
*Type:* VARIABLE
Error - file diskejected.

### ERR_FILE_EOF
*Type:* VARIABLE
Error - file eof.

### ERR_FILE_ENDOFDATA
*Type:* VARIABLE
Error - file endofdata.

### ERR_FILE_NOTFOUND
*Type:* VARIABLE
Error - file notfound.

### ERR_FORMAT
*Type:* VARIABLE
Error - format.

### ERR_HEADER_MISMATCH
*Type:* VARIABLE
Error - header mismatch.

### ERR_HTTP
*Type:* VARIABLE
Error - http.

### ERR_HTTP_ACCESS
*Type:* VARIABLE
Error - http access.

### ERR_HTTP_PROXY_AUTH
*Type:* VARIABLE
Error - http proxy auth.

### ERR_HTTP_SERVER_ERROR
*Type:* VARIABLE
Error - http server error.

### ERR_HTTP_TIMEOUT
*Type:* VARIABLE
Error - http timeout.

### ERR_INITIALIZATION
*Type:* VARIABLE
Error - initialization.

### ERR_INITIALIZED
*Type:* VARIABLE
Error - initialized.

### ERR_INTERNAL
*Type:* VARIABLE
Error - internal.

### ERR_INVALID_FLOAT
*Type:* VARIABLE
Error - invalid float.

### ERR_INVALID_HANDLE
*Type:* VARIABLE
Error - invalid handle.

### ERR_INVALID_PARAM
*Type:* VARIABLE
Error - invalid param.

### ERR_INVALID_POSITION
*Type:* VARIABLE
Error - invalid position.

### ERR_INVALID_SPEAKER
*Type:* VARIABLE
Error - invalid speaker.

### ERR_INVALID_SYNCPOINT
*Type:* VARIABLE
Error - invalid syncpoint.

### ERR_INVALID_THREAD
*Type:* VARIABLE
Error - invalid thread.

### ERR_INVALID_VECTOR
*Type:* VARIABLE
Error - invalid vector.

### ERR_MAXAUDIBLE
*Type:* VARIABLE
Error - maxaudible.

### ERR_MEMORY
*Type:* VARIABLE
Error - memory.

### ERR_MEMORY_CANTPOINT
*Type:* VARIABLE
Error - memory cantpoint.

### ERR_NEEDS3D
*Type:* VARIABLE
Error - needs3d.

### ERR_NEEDSHARDWARE
*Type:* VARIABLE
Error - needshardware.

### ERR_NET_CONNECT
*Type:* VARIABLE
Error - net connect.

### ERR_NET_SOCKET_ERROR
*Type:* VARIABLE
Error - net socket error.

### ERR_NET_URL
*Type:* VARIABLE
Error - net url.

### ERR_NET_WOULD_BLOCK
*Type:* VARIABLE
Error - net would block.

### ERR_NOTREADY
*Type:* VARIABLE
Error - notready.

### ERR_OUTPUT_ALLOCATED
*Type:* VARIABLE
Error - output allocated.

### ERR_OUTPUT_CREATEBUFFER
*Type:* VARIABLE
Error - output createbuffer.

### ERR_OUTPUT_DRIVERCALL
*Type:* VARIABLE
Error - output drivercall.

### ERR_OUTPUT_FORMAT
*Type:* VARIABLE
Error - output format.

### ERR_OUTPUT_INIT
*Type:* VARIABLE
Error - output init.

### ERR_OUTPUT_NODRIVERS
*Type:* VARIABLE
Error - output nodrivers.

### ERR_PLUGIN
*Type:* VARIABLE
Error - plugin.

### ERR_PLUGIN_MISSING
*Type:* VARIABLE
Error - plugin missing.

### ERR_PLUGIN_RESOURCE
*Type:* VARIABLE
Error - plugin resource.

### ERR_PLUGIN_VERSION
*Type:* VARIABLE
Error - plugin version.

### ERR_RECORD
*Type:* VARIABLE
Error - record.

### ERR_REVERB_CHANNELGROUP
*Type:* VARIABLE
Error - reverb channelgroup.

### ERR_REVERB_INSTANCE
*Type:* VARIABLE
Error - reverb instance.

### ERR_SUBSOUNDS
*Type:* VARIABLE
Error - subsounds.

### ERR_SUBSOUND_ALLOCATED
*Type:* VARIABLE
Error - subsound allocated.

### ERR_SUBSOUND_CANTMOVE
*Type:* VARIABLE
Error - subsound cantmove.

### ERR_TAGNOTFOUND
*Type:* VARIABLE
Error - tagnotfound.

### ERR_TOOMANYCHANNELS
*Type:* VARIABLE
Error - toomanychannels.

### ERR_TRUNCATED
*Type:* VARIABLE
Error - truncated.

### ERR_UNIMPLEMENTED
*Type:* VARIABLE
Error - unimplemented.

### ERR_UNINITIALIZED
*Type:* VARIABLE
Error - uninitialized.

### ERR_UNSUPPORTED
*Type:* VARIABLE
Error - unsupported.

### ERR_VERSION
*Type:* VARIABLE
Error - version.

### ERR_EVENT_ALREADY_LOADED
*Type:* VARIABLE
Error - event already loaded.

### ERR_EVENT_LIVEUPDATE_BUSY
*Type:* VARIABLE
Error - event liveupdate busy.

### ERR_EVENT_LIVEUPDATE_MISMATCH
*Type:* VARIABLE
Error - event liveupdate mismatch.

### ERR_EVENT_LIVEUPDATE_TIMEOUT
*Type:* VARIABLE
Error - event liveupdate timeout.

### ERR_EVENT_NOTFOUND
*Type:* VARIABLE
Error - event notfound.

### ERR_STUDIO_UNINITIALIZED
*Type:* VARIABLE
Error - studio uninitialized.

### ERR_STUDIO_NOT_LOADED
*Type:* VARIABLE
Error - studio not loaded.

### ERR_INVALID_STRING
*Type:* VARIABLE
Error - invalid string.

### ERR_ALREADY_LOCKED
*Type:* VARIABLE
Error - already locked.

### ERR_NOT_LOCKED
*Type:* VARIABLE
Error - not locked.

### ERR_RECORD_DISCONNECTED
*Type:* VARIABLE
Error - record disconnected.

### ERR_TOOMANYSAMPLES
*Type:* VARIABLE
Error - toomanysamples.

### CHANNELCONTROL_CHANNEL
*Type:* VARIABLE
Channel control type - channel.

### CHANNELCONTROL_CHANNELGROUP
*Type:* VARIABLE
Channel control type - channelgroup.

### OUTPUTTYPE_AUTODETECT
*Type:* VARIABLE
Output type - autodetect.

### OUTPUTTYPE_UNKNOWN
*Type:* VARIABLE
Output type - unknown.

### OUTPUTTYPE_NOSOUND
*Type:* VARIABLE
Output type - nosound.

### OUTPUTTYPE_WAVWRITER
*Type:* VARIABLE
Output type - wavwriter.

### OUTPUTTYPE_NOSOUND_NRT
*Type:* VARIABLE
Output type - nosound nrt.

### OUTPUTTYPE_WAVWRITER_NRT
*Type:* VARIABLE
Output type - wavwriter nrt.

### OUTPUTTYPE_WASAPI
*Type:* VARIABLE
Output type - wasapi.

### OUTPUTTYPE_ASIO
*Type:* VARIABLE
Output type - asio.

### OUTPUTTYPE_PULSEAUDIO
*Type:* VARIABLE
Output type - pulseaudio.

### OUTPUTTYPE_ALSA
*Type:* VARIABLE
Output type - alsa.

### OUTPUTTYPE_COREAUDIO
*Type:* VARIABLE
Output type - coreaudio.

### OUTPUTTYPE_AUDIOTRACK
*Type:* VARIABLE
Output type - audiotrack.

### OUTPUTTYPE_OPENSL
*Type:* VARIABLE
Output type - opensl.

### OUTPUTTYPE_AUDIOOUT
*Type:* VARIABLE
Output type - audioout.

### OUTPUTTYPE_AUDIO3D
*Type:* VARIABLE
Output type - audio3d.

### OUTPUTTYPE_WEBAUDIO
*Type:* VARIABLE
Output type - webaudio.

### OUTPUTTYPE_NNAUDIO
*Type:* VARIABLE
Output type - nnaudio.

### OUTPUTTYPE_WINSONIC
*Type:* VARIABLE
Output type - winsonic.

### OUTPUTTYPE_AAUDIO
*Type:* VARIABLE
Output type - aaudio.

### OUTPUTTYPE_AUDIOWORKLET
*Type:* VARIABLE
Output type - audioworklet.

### OUTPUTTYPE_PHASE
*Type:* VARIABLE
Output type - phase.

### OUTPUTTYPE_OHAUDIO
*Type:* VARIABLE
Output type - ohaudio.

### DEBUG_MODE_TTY
*Type:* VARIABLE
Debug mode - tty.

### DEBUG_MODE_FILE
*Type:* VARIABLE
Debug mode - file.

### DEBUG_MODE_CALLBACK
*Type:* VARIABLE
Debug mode - callback.

### SPEAKERMODE_DEFAULT
*Type:* VARIABLE
Speaker mode - default.

### SPEAKERMODE_RAW
*Type:* VARIABLE
Speaker mode - raw.

### SPEAKERMODE_MONO
*Type:* VARIABLE
Speaker mode - mono.

### SPEAKERMODE_STEREO
*Type:* VARIABLE
Speaker mode - stereo.

### SPEAKERMODE_QUAD
*Type:* VARIABLE
Speaker mode - quad.

### SPEAKERMODE_SURROUND
*Type:* VARIABLE
Speaker mode - surround.

### SPEAKERMODE_5POINT1
*Type:* VARIABLE
Speaker mode - 5point1.

### SPEAKERMODE_7POINT1
*Type:* VARIABLE
Speaker mode - 7point1.

### SPEAKERMODE_7POINT1POINT4
*Type:* VARIABLE
Speaker mode - 7point1point4.

### SPEAKER_NONE
*Type:* VARIABLE
Speaker position - none.

### SPEAKER_FRONT_LEFT
*Type:* VARIABLE
Speaker position - front left.

### SPEAKER_FRONT_RIGHT
*Type:* VARIABLE
Speaker position - front right.

### SPEAKER_FRONT_CENTER
*Type:* VARIABLE
Speaker position - front center.

### SPEAKER_LOW_FREQUENCY
*Type:* VARIABLE
Speaker position - low frequency.

### SPEAKER_SURROUND_LEFT
*Type:* VARIABLE
Speaker position - surround left.

### SPEAKER_SURROUND_RIGHT
*Type:* VARIABLE
Speaker position - surround right.

### SPEAKER_BACK_LEFT
*Type:* VARIABLE
Speaker position - back left.

### SPEAKER_BACK_RIGHT
*Type:* VARIABLE
Speaker position - back right.

### SPEAKER_TOP_FRONT_LEFT
*Type:* VARIABLE
Speaker position - top front left.

### SPEAKER_TOP_FRONT_RIGHT
*Type:* VARIABLE
Speaker position - top front right.

### SPEAKER_TOP_BACK_LEFT
*Type:* VARIABLE
Speaker position - top back left.

### SPEAKER_TOP_BACK_RIGHT
*Type:* VARIABLE
Speaker position - top back right.

### CHANNELORDER_DEFAULT
*Type:* VARIABLE
Channel order - default.

### CHANNELORDER_WAVEFORMAT
*Type:* VARIABLE
Channel order - waveformat.

### CHANNELORDER_PROTOOLS
*Type:* VARIABLE
Channel order - protools.

### CHANNELORDER_ALLMONO
*Type:* VARIABLE
Channel order - allmono.

### CHANNELORDER_ALLSTEREO
*Type:* VARIABLE
Channel order - allstereo.

### CHANNELORDER_ALSA
*Type:* VARIABLE
Channel order - alsa.

### PLUGINTYPE_OUTPUT
*Type:* VARIABLE
Plugin type - output.

### PLUGINTYPE_CODEC
*Type:* VARIABLE
Plugin type - codec.

### PLUGINTYPE_DSP
*Type:* VARIABLE
Plugin type - dsp.

### SOUND_TYPE_UNKNOWN
*Type:* VARIABLE
Sound file type - unknown.

### SOUND_TYPE_AIFF
*Type:* VARIABLE
Sound file type - aiff.

### SOUND_TYPE_ASF
*Type:* VARIABLE
Sound file type - asf.

### SOUND_TYPE_DLS
*Type:* VARIABLE
Sound file type - dls.

### SOUND_TYPE_FLAC
*Type:* VARIABLE
Sound file type - flac.

### SOUND_TYPE_FSB
*Type:* VARIABLE
Sound file type - fsb.

### SOUND_TYPE_IT
*Type:* VARIABLE
Sound file type - it.

### SOUND_TYPE_MIDI
*Type:* VARIABLE
Sound file type - midi.

### SOUND_TYPE_MOD
*Type:* VARIABLE
Sound file type - mod.

### SOUND_TYPE_MPEG
*Type:* VARIABLE
Sound file type - mpeg.

### SOUND_TYPE_OGGVORBIS
*Type:* VARIABLE
Sound file type - oggvorbis.

### SOUND_TYPE_PLAYLIST
*Type:* VARIABLE
Sound file type - playlist.

### SOUND_TYPE_RAW
*Type:* VARIABLE
Sound file type - raw.

### SOUND_TYPE_S3M
*Type:* VARIABLE
Sound file type - s3m.

### SOUND_TYPE_USER
*Type:* VARIABLE
Sound file type - user.

### SOUND_TYPE_WAV
*Type:* VARIABLE
Sound file type - wav.

### SOUND_TYPE_XM
*Type:* VARIABLE
Sound file type - xm.

### SOUND_TYPE_XMA
*Type:* VARIABLE
Sound file type - xma.

### SOUND_TYPE_AUDIOQUEUE
*Type:* VARIABLE
Sound file type - audioqueue.

### SOUND_TYPE_AT9
*Type:* VARIABLE
Sound file type - at9.

### SOUND_TYPE_VORBIS
*Type:* VARIABLE
Sound file type - vorbis.

### SOUND_TYPE_MEDIA_FOUNDATION
*Type:* VARIABLE
Sound file type - media foundation.

### SOUND_TYPE_MEDIACODEC
*Type:* VARIABLE
Sound file type - mediacodec.

### SOUND_TYPE_FADPCM
*Type:* VARIABLE
Sound file type - fadpcm.

### SOUND_TYPE_OPUS
*Type:* VARIABLE
Sound file type - opus.

### SOUND_FORMAT_NONE
*Type:* VARIABLE
Sound data format - none.

### SOUND_FORMAT_PCM8
*Type:* VARIABLE
Sound data format - pcm8.

### SOUND_FORMAT_PCM16
*Type:* VARIABLE
Sound data format - pcm16.

### SOUND_FORMAT_PCM24
*Type:* VARIABLE
Sound data format - pcm24.

### SOUND_FORMAT_PCM32
*Type:* VARIABLE
Sound data format - pcm32.

### SOUND_FORMAT_PCMFLOAT
*Type:* VARIABLE
Sound data format - pcmfloat.

### SOUND_FORMAT_BITSTREAM
*Type:* VARIABLE
Sound data format - bitstream.

### OPENSTATE_READY
*Type:* VARIABLE
Open state - ready.

### OPENSTATE_LOADING
*Type:* VARIABLE
Open state - loading.

### OPENSTATE_ERROR
*Type:* VARIABLE
Open state - error.

### OPENSTATE_CONNECTING
*Type:* VARIABLE
Open state - connecting.

### OPENSTATE_BUFFERING
*Type:* VARIABLE
Open state - buffering.

### OPENSTATE_SEEKING
*Type:* VARIABLE
Open state - seeking.

### OPENSTATE_PLAYING
*Type:* VARIABLE
Open state - playing.

### OPENSTATE_SETPOSITION
*Type:* VARIABLE
Open state - setposition.

### SOUNDGROUP_BEHAVIOR_FAIL
*Type:* VARIABLE
Sound group behavior - fail.

### SOUNDGROUP_BEHAVIOR_MUTE
*Type:* VARIABLE
Sound group behavior - mute.

### SOUNDGROUP_BEHAVIOR_STEALLOWEST
*Type:* VARIABLE
Sound group behavior - steallowest.

### CHANNELCONTROL_CALLBACK_END
*Type:* VARIABLE
Channel control callback - end.

### CHANNELCONTROL_CALLBACK_VIRTUALVOICE
*Type:* VARIABLE
Channel control callback - virtualvoice.

### CHANNELCONTROL_CALLBACK_SYNCPOINT
*Type:* VARIABLE
Channel control callback - syncpoint.

### CHANNELCONTROL_CALLBACK_OCCLUSION
*Type:* VARIABLE
Channel control callback - occlusion.

### CHANNELCONTROL_DSP_HEAD
*Type:* VARIABLE
Channel control type - dsp head.

### CHANNELCONTROL_DSP_FADER
*Type:* VARIABLE
Channel control type - dsp fader.

### CHANNELCONTROL_DSP_TAIL
*Type:* VARIABLE
Channel control type - dsp tail.

### ERRORCALLBACK_INSTANCETYPE_NONE
*Type:* VARIABLE
Errorcallback instancetype none.

### ERRORCALLBACK_INSTANCETYPE_SYSTEM
*Type:* VARIABLE
Errorcallback instancetype system.

### ERRORCALLBACK_INSTANCETYPE_CHANNEL
*Type:* VARIABLE
Errorcallback instancetype channel.

### ERRORCALLBACK_INSTANCETYPE_CHANNELGROUP
*Type:* VARIABLE
Errorcallback instancetype channelgroup.

### ERRORCALLBACK_INSTANCETYPE_CHANNELCONTROL
*Type:* VARIABLE
Errorcallback instancetype channelcontrol.

### ERRORCALLBACK_INSTANCETYPE_SOUND
*Type:* VARIABLE
Errorcallback instancetype sound.

### ERRORCALLBACK_INSTANCETYPE_SOUNDGROUP
*Type:* VARIABLE
Errorcallback instancetype soundgroup.

### ERRORCALLBACK_INSTANCETYPE_DSP
*Type:* VARIABLE
Errorcallback instancetype dsp.

### ERRORCALLBACK_INSTANCETYPE_DSPCONNECTION
*Type:* VARIABLE
Errorcallback instancetype dspconnection.

### ERRORCALLBACK_INSTANCETYPE_GEOMETRY
*Type:* VARIABLE
Errorcallback instancetype geometry.

### ERRORCALLBACK_INSTANCETYPE_REVERB3D
*Type:* VARIABLE
Errorcallback instancetype reverb3d.

### ERRORCALLBACK_INSTANCETYPE_STUDIO_SYSTEM
*Type:* VARIABLE
Errorcallback instancetype studio system.

### ERRORCALLBACK_INSTANCETYPE_STUDIO_EVENTDESCRIPTION
*Type:* VARIABLE
Errorcallback instancetype studio eventdescription.

### ERRORCALLBACK_INSTANCETYPE_STUDIO_EVENTINSTANCE
*Type:* VARIABLE
Errorcallback instancetype studio eventinstance.

### ERRORCALLBACK_INSTANCETYPE_STUDIO_PARAMETERINSTANCE
*Type:* VARIABLE
Errorcallback instancetype studio parameterinstance.

### ERRORCALLBACK_INSTANCETYPE_STUDIO_BUS
*Type:* VARIABLE
Errorcallback instancetype studio bus.

### ERRORCALLBACK_INSTANCETYPE_STUDIO_VCA
*Type:* VARIABLE
Errorcallback instancetype studio vca.

### ERRORCALLBACK_INSTANCETYPE_STUDIO_BANK
*Type:* VARIABLE
Errorcallback instancetype studio bank.

### ERRORCALLBACK_INSTANCETYPE_STUDIO_COMMANDREPLAY
*Type:* VARIABLE
Errorcallback instancetype studio commandreplay.

### DSP_RESAMPLER_DEFAULT
*Type:* VARIABLE
DSP resampler - default.

### DSP_RESAMPLER_NOINTERP
*Type:* VARIABLE
DSP resampler - nointerp.

### DSP_RESAMPLER_LINEAR
*Type:* VARIABLE
DSP resampler - linear.

### DSP_RESAMPLER_CUBIC
*Type:* VARIABLE
DSP resampler - cubic.

### DSP_RESAMPLER_SPLINE
*Type:* VARIABLE
DSP resampler - spline.

### DSP_CALLBACK_DATAPARAMETERRELEASE
*Type:* VARIABLE
DSP callback type - dataparameterrelease.

### DSPCONNECTION_TYPE_STANDARD
*Type:* VARIABLE
DSP connection type - standard.

### DSPCONNECTION_TYPE_SIDECHAIN
*Type:* VARIABLE
DSP connection type - sidechain.

### DSPCONNECTION_TYPE_SEND
*Type:* VARIABLE
DSP connection type - send.

### DSPCONNECTION_TYPE_SEND_SIDECHAIN
*Type:* VARIABLE
DSP connection type - send sidechain.

### DSPCONNECTION_TYPE_PREALLOCATED
*Type:* VARIABLE
DSP connection type - preallocated.

### TAGTYPE_UNKNOWN
*Type:* VARIABLE
Tag type - unknown.

### TAGTYPE_ID3V1
*Type:* VARIABLE
Tag type - id3v1.

### TAGTYPE_ID3V2
*Type:* VARIABLE
Tag type - id3v2.

### TAGTYPE_VORBISCOMMENT
*Type:* VARIABLE
Tag type - vorbiscomment.

### TAGTYPE_SHOUTCAST
*Type:* VARIABLE
Tag type - shoutcast.

### TAGTYPE_ICECAST
*Type:* VARIABLE
Tag type - icecast.

### TAGTYPE_ASF
*Type:* VARIABLE
Tag type - asf.

### TAGTYPE_MIDI
*Type:* VARIABLE
Tag type - midi.

### TAGTYPE_PLAYLIST
*Type:* VARIABLE
Tag type - playlist.

### TAGTYPE_FMOD
*Type:* VARIABLE
Tag type - fmod.

### TAGTYPE_USER
*Type:* VARIABLE
Tag type - user.

### TAGDATATYPE_BINARY
*Type:* VARIABLE
Tag data type - binary.

### TAGDATATYPE_INT
*Type:* VARIABLE
Tag data type - int.

### TAGDATATYPE_FLOAT
*Type:* VARIABLE
Tag data type - float.

### TAGDATATYPE_STRING
*Type:* VARIABLE
Tag data type - string.

### TAGDATATYPE_STRING_UTF16
*Type:* VARIABLE
Tag data type - string utf16.

### TAGDATATYPE_STRING_UTF16BE
*Type:* VARIABLE
Tag data type - string utf16be.

### TAGDATATYPE_STRING_UTF8
*Type:* VARIABLE
Tag data type - string utf8.

### PORT_TYPE_MUSIC
*Type:* VARIABLE
Port type - music.

### PORT_TYPE_COPYRIGHT_MUSIC
*Type:* VARIABLE
Port type - copyright music.

### PORT_TYPE_VOICE
*Type:* VARIABLE
Port type - voice.

### PORT_TYPE_CONTROLLER
*Type:* VARIABLE
Port type - controller.

### PORT_TYPE_PERSONAL
*Type:* VARIABLE
Port type - personal.

### PORT_TYPE_VIBRATION
*Type:* VARIABLE
Port type - vibration.

### PORT_TYPE_AUX
*Type:* VARIABLE
Port type - aux.

### PORT_TYPE_PASSTHROUGH
*Type:* VARIABLE
Port type - passthrough.

### PORT_TYPE_VR_VIBRATION
*Type:* VARIABLE
Port type - vr vibration.

### DSP_TYPE_UNKNOWN
*Type:* VARIABLE
DSP effect type - unknown.

### DSP_TYPE_MIXER
*Type:* VARIABLE
DSP effect type - mixer.

### DSP_TYPE_OSCILLATOR
*Type:* VARIABLE
DSP effect type - oscillator.

### DSP_TYPE_LOWPASS
*Type:* VARIABLE
DSP effect type - lowpass.

### DSP_TYPE_ITLOWPASS
*Type:* VARIABLE
DSP effect type - itlowpass.

### DSP_TYPE_HIGHPASS
*Type:* VARIABLE
DSP effect type - highpass.

### DSP_TYPE_ECHO
*Type:* VARIABLE
DSP effect type - echo.

### DSP_TYPE_FADER
*Type:* VARIABLE
DSP effect type - fader.

### DSP_TYPE_FLANGE
*Type:* VARIABLE
DSP effect type - flange.

### DSP_TYPE_DISTORTION
*Type:* VARIABLE
DSP effect type - distortion.

### DSP_TYPE_NORMALIZE
*Type:* VARIABLE
DSP effect type - normalize.

### DSP_TYPE_LIMITER
*Type:* VARIABLE
DSP effect type - limiter.

### DSP_TYPE_PARAMEQ
*Type:* VARIABLE
DSP effect type - parameq.

### DSP_TYPE_PITCHSHIFT
*Type:* VARIABLE
DSP effect type - pitchshift.

### DSP_TYPE_CHORUS
*Type:* VARIABLE
DSP effect type - chorus.

### DSP_TYPE_ITECHO
*Type:* VARIABLE
DSP effect type - itecho.

### DSP_TYPE_COMPRESSOR
*Type:* VARIABLE
DSP effect type - compressor.

### DSP_TYPE_SFXREVERB
*Type:* VARIABLE
DSP effect type - sfxreverb.

### DSP_TYPE_LOWPASS_SIMPLE
*Type:* VARIABLE
DSP effect type - lowpass simple.

### DSP_TYPE_DELAY
*Type:* VARIABLE
DSP effect type - delay.

### DSP_TYPE_TREMOLO
*Type:* VARIABLE
DSP effect type - tremolo.

### DSP_TYPE_SEND
*Type:* VARIABLE
DSP effect type - send.

### DSP_TYPE_RETURN
*Type:* VARIABLE
DSP effect type - return.

### DSP_TYPE_HIGHPASS_SIMPLE
*Type:* VARIABLE
DSP effect type - highpass simple.

### DSP_TYPE_PAN
*Type:* VARIABLE
DSP effect type - pan.

### DSP_TYPE_THREE_EQ
*Type:* VARIABLE
DSP effect type - three eq.

### DSP_TYPE_FFT
*Type:* VARIABLE
DSP effect type - fft.

### DSP_TYPE_LOUDNESS_METER
*Type:* VARIABLE
DSP effect type - loudness meter.

### DSP_TYPE_CONVOLUTIONREVERB
*Type:* VARIABLE
DSP effect type - convolutionreverb.

### DSP_TYPE_CHANNELMIX
*Type:* VARIABLE
DSP effect type - channelmix.

### DSP_TYPE_TRANSCEIVER
*Type:* VARIABLE
DSP effect type - transceiver.

### DSP_TYPE_OBJECTPAN
*Type:* VARIABLE
DSP effect type - objectpan.

### DSP_TYPE_MULTIBAND_EQ
*Type:* VARIABLE
DSP effect type - multiband eq.

### DSP_TYPE_MULTIBAND_DYNAMICS
*Type:* VARIABLE
DSP effect type - multiband dynamics.

### DSP_OSCILLATOR_TYPE
*Type:* VARIABLE
Dsp oscillator type.

### DSP_OSCILLATOR_RATE
*Type:* VARIABLE
Dsp oscillator rate.

### DSP_LOWPASS_CUTOFF
*Type:* VARIABLE
Dsp lowpass cutoff.

### DSP_LOWPASS_RESONANCE
*Type:* VARIABLE
Dsp lowpass resonance.

### DSP_ITLOWPASS_CUTOFF
*Type:* VARIABLE
Dsp itlowpass cutoff.

### DSP_ITLOWPASS_RESONANCE
*Type:* VARIABLE
Dsp itlowpass resonance.

### DSP_HIGHPASS_CUTOFF
*Type:* VARIABLE
Dsp highpass cutoff.

### DSP_HIGHPASS_RESONANCE
*Type:* VARIABLE
Dsp highpass resonance.

### DSP_ECHO_DELAY
*Type:* VARIABLE
Dsp echo delay.

### DSP_ECHO_FEEDBACK
*Type:* VARIABLE
Dsp echo feedback.

### DSP_ECHO_DRYLEVEL
*Type:* VARIABLE
Dsp echo drylevel.

### DSP_ECHO_WETLEVEL
*Type:* VARIABLE
Dsp echo wetlevel.

### DSP_ECHO_DELAYCHANGEMODE
*Type:* VARIABLE
Dsp echo delaychangemode.

### DSP_ECHO_DELAYCHANGEMODE_FADE
*Type:* VARIABLE
Dsp echo delaychangemode fade.

### DSP_ECHO_DELAYCHANGEMODE_LERP
*Type:* VARIABLE
Dsp echo delaychangemode lerp.

### DSP_ECHO_DELAYCHANGEMODE_NONE
*Type:* VARIABLE
Dsp echo delaychangemode none.

### DSP_FADER_GAIN
*Type:* VARIABLE
Dsp fader gain.

### DSP_FADER_OVERALL_GAIN
*Type:* VARIABLE
Dsp fader overall gain.

### DSP_FLANGE_MIX
*Type:* VARIABLE
Dsp flange mix.

### DSP_FLANGE_DEPTH
*Type:* VARIABLE
Dsp flange depth.

### DSP_FLANGE_RATE
*Type:* VARIABLE
Dsp flange rate.

### DSP_DISTORTION_LEVEL
*Type:* VARIABLE
Dsp distortion level.

### DSP_NORMALIZE_FADETIME
*Type:* VARIABLE
Dsp normalize fadetime.

### DSP_NORMALIZE_THRESHOLD
*Type:* VARIABLE
Dsp normalize threshold.

### DSP_NORMALIZE_MAXAMP
*Type:* VARIABLE
Dsp normalize maxamp.

### DSP_LIMITER_RELEASETIME
*Type:* VARIABLE
Dsp limiter releasetime.

### DSP_LIMITER_CEILING
*Type:* VARIABLE
Dsp limiter ceiling.

### DSP_LIMITER_MAXIMIZERGAIN
*Type:* VARIABLE
Dsp limiter maximizergain.

### DSP_LIMITER_MODE
*Type:* VARIABLE
Dsp limiter mode.

### DSP_PARAMEQ_CENTER
*Type:* VARIABLE
Dsp parameq center.

### DSP_PARAMEQ_BANDWIDTH
*Type:* VARIABLE
Dsp parameq bandwidth.

### DSP_PARAMEQ_GAIN
*Type:* VARIABLE
Dsp parameq gain.

### DSP_MULTIBAND_EQ_A_FILTER
*Type:* VARIABLE
Dsp multiband eq a filter.

### DSP_MULTIBAND_EQ_A_FREQUENCY
*Type:* VARIABLE
Dsp multiband eq a frequency.

### DSP_MULTIBAND_EQ_A_Q
*Type:* VARIABLE
Dsp multiband eq a q.

### DSP_MULTIBAND_EQ_A_GAIN
*Type:* VARIABLE
Dsp multiband eq a gain.

### DSP_MULTIBAND_EQ_B_FILTER
*Type:* VARIABLE
Dsp multiband eq b filter.

### DSP_MULTIBAND_EQ_B_FREQUENCY
*Type:* VARIABLE
Dsp multiband eq b frequency.

### DSP_MULTIBAND_EQ_B_Q
*Type:* VARIABLE
Dsp multiband eq b q.

### DSP_MULTIBAND_EQ_B_GAIN
*Type:* VARIABLE
Dsp multiband eq b gain.

### DSP_MULTIBAND_EQ_C_FILTER
*Type:* VARIABLE
Dsp multiband eq c filter.

### DSP_MULTIBAND_EQ_C_FREQUENCY
*Type:* VARIABLE
Dsp multiband eq c frequency.

### DSP_MULTIBAND_EQ_C_Q
*Type:* VARIABLE
Dsp multiband eq c q.

### DSP_MULTIBAND_EQ_C_GAIN
*Type:* VARIABLE
Dsp multiband eq c gain.

### DSP_MULTIBAND_EQ_D_FILTER
*Type:* VARIABLE
Dsp multiband eq d filter.

### DSP_MULTIBAND_EQ_D_FREQUENCY
*Type:* VARIABLE
Dsp multiband eq d frequency.

### DSP_MULTIBAND_EQ_D_Q
*Type:* VARIABLE
Dsp multiband eq d q.

### DSP_MULTIBAND_EQ_D_GAIN
*Type:* VARIABLE
Dsp multiband eq d gain.

### DSP_MULTIBAND_EQ_E_FILTER
*Type:* VARIABLE
Dsp multiband eq e filter.

### DSP_MULTIBAND_EQ_E_FREQUENCY
*Type:* VARIABLE
Dsp multiband eq e frequency.

### DSP_MULTIBAND_EQ_E_Q
*Type:* VARIABLE
Dsp multiband eq e q.

### DSP_MULTIBAND_EQ_E_GAIN
*Type:* VARIABLE
Dsp multiband eq e gain.

### DSP_MULTIBAND_EQ_FILTER_DISABLED
*Type:* VARIABLE
Dsp multiband eq filter disabled.

### DSP_MULTIBAND_EQ_FILTER_LOWPASS_12DB
*Type:* VARIABLE
Dsp multiband eq filter lowpass 12db.

### DSP_MULTIBAND_EQ_FILTER_LOWPASS_24DB
*Type:* VARIABLE
Dsp multiband eq filter lowpass 24db.

### DSP_MULTIBAND_EQ_FILTER_LOWPASS_48DB
*Type:* VARIABLE
Dsp multiband eq filter lowpass 48db.

### DSP_MULTIBAND_EQ_FILTER_HIGHPASS_12DB
*Type:* VARIABLE
Dsp multiband eq filter highpass 12db.

### DSP_MULTIBAND_EQ_FILTER_HIGHPASS_24DB
*Type:* VARIABLE
Dsp multiband eq filter highpass 24db.

### DSP_MULTIBAND_EQ_FILTER_HIGHPASS_48DB
*Type:* VARIABLE
Dsp multiband eq filter highpass 48db.

### DSP_MULTIBAND_EQ_FILTER_LOWSHELF
*Type:* VARIABLE
Dsp multiband eq filter lowshelf.

### DSP_MULTIBAND_EQ_FILTER_HIGHSHELF
*Type:* VARIABLE
Dsp multiband eq filter highshelf.

### DSP_MULTIBAND_EQ_FILTER_PEAKING
*Type:* VARIABLE
Dsp multiband eq filter peaking.

### DSP_MULTIBAND_EQ_FILTER_BANDPASS
*Type:* VARIABLE
Dsp multiband eq filter bandpass.

### DSP_MULTIBAND_EQ_FILTER_NOTCH
*Type:* VARIABLE
Dsp multiband eq filter notch.

### DSP_MULTIBAND_EQ_FILTER_ALLPASS
*Type:* VARIABLE
Dsp multiband eq filter allpass.

### DSP_MULTIBAND_EQ_FILTER_LOWPASS_6DB
*Type:* VARIABLE
Dsp multiband eq filter lowpass 6db.

### DSP_MULTIBAND_EQ_FILTER_HIGHPASS_6DB
*Type:* VARIABLE
Dsp multiband eq filter highpass 6db.

### DSP_MULTIBAND_DYNAMICS_LOWER_FREQUENCY
*Type:* VARIABLE
Dsp multiband dynamics lower frequency.

### DSP_MULTIBAND_DYNAMICS_UPPER_FREQUENCY
*Type:* VARIABLE
Dsp multiband dynamics upper frequency.

### DSP_MULTIBAND_DYNAMICS_LINKED
*Type:* VARIABLE
Dsp multiband dynamics linked.

### DSP_MULTIBAND_DYNAMICS_USE_SIDECHAIN
*Type:* VARIABLE
Dsp multiband dynamics use sidechain.

### DSP_MULTIBAND_DYNAMICS_A_MODE
*Type:* VARIABLE
Dsp multiband dynamics a mode.

### DSP_MULTIBAND_DYNAMICS_A_GAIN
*Type:* VARIABLE
Dsp multiband dynamics a gain.

### DSP_MULTIBAND_DYNAMICS_A_THRESHOLD
*Type:* VARIABLE
Dsp multiband dynamics a threshold.

### DSP_MULTIBAND_DYNAMICS_A_RATIO
*Type:* VARIABLE
Dsp multiband dynamics a ratio.

### DSP_MULTIBAND_DYNAMICS_A_ATTACK
*Type:* VARIABLE
Dsp multiband dynamics a attack.

### DSP_MULTIBAND_DYNAMICS_A_RELEASE
*Type:* VARIABLE
Dsp multiband dynamics a release.

### DSP_MULTIBAND_DYNAMICS_A_GAIN_MAKEUP
*Type:* VARIABLE
Dsp multiband dynamics a gain makeup.

### DSP_MULTIBAND_DYNAMICS_A_RESPONSE_DATA
*Type:* VARIABLE
Dsp multiband dynamics a response data.

### DSP_MULTIBAND_DYNAMICS_B_MODE
*Type:* VARIABLE
Dsp multiband dynamics b mode.

### DSP_MULTIBAND_DYNAMICS_B_GAIN
*Type:* VARIABLE
Dsp multiband dynamics b gain.

### DSP_MULTIBAND_DYNAMICS_B_THRESHOLD
*Type:* VARIABLE
Dsp multiband dynamics b threshold.

### DSP_MULTIBAND_DYNAMICS_B_RATIO
*Type:* VARIABLE
Dsp multiband dynamics b ratio.

### DSP_MULTIBAND_DYNAMICS_B_ATTACK
*Type:* VARIABLE
Dsp multiband dynamics b attack.

### DSP_MULTIBAND_DYNAMICS_B_RELEASE
*Type:* VARIABLE
Dsp multiband dynamics b release.

### DSP_MULTIBAND_DYNAMICS_B_GAIN_MAKEUP
*Type:* VARIABLE
Dsp multiband dynamics b gain makeup.

### DSP_MULTIBAND_DYNAMICS_B_RESPONSE_DATA
*Type:* VARIABLE
Dsp multiband dynamics b response data.

### DSP_MULTIBAND_DYNAMICS_C_MODE
*Type:* VARIABLE
Dsp multiband dynamics c mode.

### DSP_MULTIBAND_DYNAMICS_C_GAIN
*Type:* VARIABLE
Dsp multiband dynamics c gain.

### DSP_MULTIBAND_DYNAMICS_C_THRESHOLD
*Type:* VARIABLE
Dsp multiband dynamics c threshold.

### DSP_MULTIBAND_DYNAMICS_C_RATIO
*Type:* VARIABLE
Dsp multiband dynamics c ratio.

### DSP_MULTIBAND_DYNAMICS_C_ATTACK
*Type:* VARIABLE
Dsp multiband dynamics c attack.

### DSP_MULTIBAND_DYNAMICS_C_RELEASE
*Type:* VARIABLE
Dsp multiband dynamics c release.

### DSP_MULTIBAND_DYNAMICS_C_GAIN_MAKEUP
*Type:* VARIABLE
Dsp multiband dynamics c gain makeup.

### DSP_MULTIBAND_DYNAMICS_C_RESPONSE_DATA
*Type:* VARIABLE
Dsp multiband dynamics c response data.

### DSP_MULTIBAND_DYNAMICS_MODE_DISABLED
*Type:* VARIABLE
Dsp multiband dynamics mode disabled.

### DSP_MULTIBAND_DYNAMICS_MODE_COMPRESS_UP
*Type:* VARIABLE
Dsp multiband dynamics mode compress up.

### DSP_MULTIBAND_DYNAMICS_MODE_COMPRESS_DOWN
*Type:* VARIABLE
Dsp multiband dynamics mode compress down.

### DSP_MULTIBAND_DYNAMICS_MODE_EXPAND_UP
*Type:* VARIABLE
Dsp multiband dynamics mode expand up.

### DSP_MULTIBAND_DYNAMICS_MODE_EXPAND_DOWN
*Type:* VARIABLE
Dsp multiband dynamics mode expand down.

### DSP_PITCHSHIFT_PITCH
*Type:* VARIABLE
Dsp pitchshift pitch.

### DSP_PITCHSHIFT_FFTSIZE
*Type:* VARIABLE
Dsp pitchshift fftsize.

### DSP_PITCHSHIFT_OVERLAP
*Type:* VARIABLE
Dsp pitchshift overlap.

### DSP_PITCHSHIFT_MAXCHANNELS
*Type:* VARIABLE
Dsp pitchshift maxchannels.

### DSP_CHORUS_MIX
*Type:* VARIABLE
Dsp chorus mix.

### DSP_CHORUS_RATE
*Type:* VARIABLE
Dsp chorus rate.

### DSP_CHORUS_DEPTH
*Type:* VARIABLE
Dsp chorus depth.

### DSP_ITECHO_WETDRYMIX
*Type:* VARIABLE
Dsp itecho wetdrymix.

### DSP_ITECHO_FEEDBACK
*Type:* VARIABLE
Dsp itecho feedback.

### DSP_ITECHO_LEFTDELAY
*Type:* VARIABLE
Dsp itecho leftdelay.

### DSP_ITECHO_RIGHTDELAY
*Type:* VARIABLE
Dsp itecho rightdelay.

### DSP_ITECHO_PANDELAY
*Type:* VARIABLE
Dsp itecho pandelay.

### DSP_COMPRESSOR_THRESHOLD
*Type:* VARIABLE
Dsp compressor threshold.

### DSP_COMPRESSOR_RATIO
*Type:* VARIABLE
Dsp compressor ratio.

### DSP_COMPRESSOR_ATTACK
*Type:* VARIABLE
Dsp compressor attack.

### DSP_COMPRESSOR_RELEASE
*Type:* VARIABLE
Dsp compressor release.

### DSP_COMPRESSOR_GAINMAKEUP
*Type:* VARIABLE
Dsp compressor gainmakeup.

### DSP_COMPRESSOR_USESIDECHAIN
*Type:* VARIABLE
Dsp compressor usesidechain.

### DSP_COMPRESSOR_LINKED
*Type:* VARIABLE
Dsp compressor linked.

### DSP_SFXREVERB_DECAYTIME
*Type:* VARIABLE
Dsp sfxreverb decaytime.

### DSP_SFXREVERB_EARLYDELAY
*Type:* VARIABLE
Dsp sfxreverb earlydelay.

### DSP_SFXREVERB_LATEDELAY
*Type:* VARIABLE
Dsp sfxreverb latedelay.

### DSP_SFXREVERB_HFREFERENCE
*Type:* VARIABLE
Dsp sfxreverb hfreference.

### DSP_SFXREVERB_HFDECAYRATIO
*Type:* VARIABLE
Dsp sfxreverb hfdecayratio.

### DSP_SFXREVERB_DIFFUSION
*Type:* VARIABLE
Dsp sfxreverb diffusion.

### DSP_SFXREVERB_DENSITY
*Type:* VARIABLE
Dsp sfxreverb density.

### DSP_SFXREVERB_LOWSHELFFREQUENCY
*Type:* VARIABLE
Dsp sfxreverb lowshelffrequency.

### DSP_SFXREVERB_LOWSHELFGAIN
*Type:* VARIABLE
Dsp sfxreverb lowshelfgain.

### DSP_SFXREVERB_HIGHCUT
*Type:* VARIABLE
Dsp sfxreverb highcut.

### DSP_SFXREVERB_EARLYLATEMIX
*Type:* VARIABLE
Dsp sfxreverb earlylatemix.

### DSP_SFXREVERB_WETLEVEL
*Type:* VARIABLE
Dsp sfxreverb wetlevel.

### DSP_SFXREVERB_DRYLEVEL
*Type:* VARIABLE
Dsp sfxreverb drylevel.

### DSP_LOWPASS_SIMPLE_CUTOFF
*Type:* VARIABLE
Dsp lowpass simple cutoff.

### DSP_DELAY_CH0
*Type:* VARIABLE
Dsp delay ch0.

### DSP_DELAY_CH1
*Type:* VARIABLE
Dsp delay ch1.

### DSP_DELAY_CH2
*Type:* VARIABLE
Dsp delay ch2.

### DSP_DELAY_CH3
*Type:* VARIABLE
Dsp delay ch3.

### DSP_DELAY_CH4
*Type:* VARIABLE
Dsp delay ch4.

### DSP_DELAY_CH5
*Type:* VARIABLE
Dsp delay ch5.

### DSP_DELAY_CH6
*Type:* VARIABLE
Dsp delay ch6.

### DSP_DELAY_CH7
*Type:* VARIABLE
Dsp delay ch7.

### DSP_DELAY_CH8
*Type:* VARIABLE
Dsp delay ch8.

### DSP_DELAY_CH9
*Type:* VARIABLE
Dsp delay ch9.

### DSP_DELAY_CH10
*Type:* VARIABLE
Dsp delay ch10.

### DSP_DELAY_CH11
*Type:* VARIABLE
Dsp delay ch11.

### DSP_DELAY_CH12
*Type:* VARIABLE
Dsp delay ch12.

### DSP_DELAY_CH13
*Type:* VARIABLE
Dsp delay ch13.

### DSP_DELAY_CH14
*Type:* VARIABLE
Dsp delay ch14.

### DSP_DELAY_CH15
*Type:* VARIABLE
Dsp delay ch15.

### DSP_DELAY_MAXDELAY
*Type:* VARIABLE
Dsp delay maxdelay.

### DSP_TREMOLO_FREQUENCY
*Type:* VARIABLE
Dsp tremolo frequency.

### DSP_TREMOLO_DEPTH
*Type:* VARIABLE
Dsp tremolo depth.

### DSP_TREMOLO_SHAPE
*Type:* VARIABLE
Dsp tremolo shape.

### DSP_TREMOLO_SKEW
*Type:* VARIABLE
Dsp tremolo skew.

### DSP_TREMOLO_DUTY
*Type:* VARIABLE
Dsp tremolo duty.

### DSP_TREMOLO_SQUARE
*Type:* VARIABLE
Dsp tremolo square.

### DSP_TREMOLO_PHASE
*Type:* VARIABLE
Dsp tremolo phase.

### DSP_TREMOLO_SPREAD
*Type:* VARIABLE
Dsp tremolo spread.

### DSP_SEND_RETURNID
*Type:* VARIABLE
Dsp send returnid.

### DSP_SEND_LEVEL
*Type:* VARIABLE
Dsp send level.

### DSP_RETURN_ID
*Type:* VARIABLE
Dsp return id.

### DSP_RETURN_INPUT_SPEAKER_MODE
*Type:* VARIABLE
Dsp return input speaker mode.

### DSP_HIGHPASS_SIMPLE_CUTOFF
*Type:* VARIABLE
Dsp highpass simple cutoff.

### DSP_PAN_2D_STEREO_MODE_DISTRIBUTED
*Type:* VARIABLE
Dsp pan 2d stereo mode distributed.

### DSP_PAN_2D_STEREO_MODE_DISCRETE
*Type:* VARIABLE
Dsp pan 2d stereo mode discrete.

### DSP_PAN_MODE_MONO
*Type:* VARIABLE
Dsp pan mode mono.

### DSP_PAN_MODE_STEREO
*Type:* VARIABLE
Dsp pan mode stereo.

### DSP_PAN_MODE_SURROUND
*Type:* VARIABLE
Dsp pan mode surround.

### DSP_PAN_3D_ROLLOFF_LINEARSQUARED
*Type:* VARIABLE
Pan 3D rolloff type - linearsquared.

### DSP_PAN_3D_ROLLOFF_LINEAR
*Type:* VARIABLE
Pan 3D rolloff type - linear.

### DSP_PAN_3D_ROLLOFF_INVERSE
*Type:* VARIABLE
Pan 3D rolloff type - inverse.

### DSP_PAN_3D_ROLLOFF_INVERSETAPERED
*Type:* VARIABLE
Pan 3D rolloff type - inversetapered.

### DSP_PAN_3D_ROLLOFF_CUSTOM
*Type:* VARIABLE
Pan 3D rolloff type - custom.

### DSP_PAN_3D_EXTENT_MODE_AUTO
*Type:* VARIABLE
Dsp pan 3d extent mode auto.

### DSP_PAN_3D_EXTENT_MODE_USER
*Type:* VARIABLE
Dsp pan 3d extent mode user.

### DSP_PAN_3D_EXTENT_MODE_OFF
*Type:* VARIABLE
Dsp pan 3d extent mode off.

### DSP_PAN_MODE
*Type:* VARIABLE
Dsp pan mode.

### DSP_PAN_2D_STEREO_POSITION
*Type:* VARIABLE
Dsp pan 2d stereo position.

### DSP_PAN_2D_DIRECTION
*Type:* VARIABLE
Dsp pan 2d direction.

### DSP_PAN_2D_EXTENT
*Type:* VARIABLE
Dsp pan 2d extent.

### DSP_PAN_2D_ROTATION
*Type:* VARIABLE
Dsp pan 2d rotation.

### DSP_PAN_2D_LFE_LEVEL
*Type:* VARIABLE
Dsp pan 2d lfe level.

### DSP_PAN_2D_STEREO_MODE
*Type:* VARIABLE
Dsp pan 2d stereo mode.

### DSP_PAN_2D_STEREO_SEPARATION
*Type:* VARIABLE
Dsp pan 2d stereo separation.

### DSP_PAN_2D_STEREO_AXIS
*Type:* VARIABLE
Dsp pan 2d stereo axis.

### DSP_PAN_ENABLED_SPEAKERS
*Type:* VARIABLE
Dsp pan enabled speakers.

### DSP_PAN_3D_POSITION
*Type:* VARIABLE
Dsp pan 3d position.

### DSP_PAN_3D_ROLLOFF
*Type:* VARIABLE
Dsp pan 3d rolloff.

### DSP_PAN_3D_MIN_DISTANCE
*Type:* VARIABLE
Dsp pan 3d min distance.

### DSP_PAN_3D_MAX_DISTANCE
*Type:* VARIABLE
Dsp pan 3d max distance.

### DSP_PAN_3D_EXTENT_MODE
*Type:* VARIABLE
Dsp pan 3d extent mode.

### DSP_PAN_3D_SOUND_SIZE
*Type:* VARIABLE
Dsp pan 3d sound size.

### DSP_PAN_3D_MIN_EXTENT
*Type:* VARIABLE
Dsp pan 3d min extent.

### DSP_PAN_3D_PAN_BLEND
*Type:* VARIABLE
Dsp pan 3d pan blend.

### DSP_PAN_LFE_UPMIX_ENABLED
*Type:* VARIABLE
Dsp pan lfe upmix enabled.

### DSP_PAN_OVERALL_GAIN
*Type:* VARIABLE
Dsp pan overall gain.

### DSP_PAN_SURROUND_SPEAKER_MODE
*Type:* VARIABLE
Pan surround mode - speaker mode.

### DSP_PAN_2D_HEIGHT_BLEND
*Type:* VARIABLE
Dsp pan 2d height blend.

### DSP_PAN_ATTENUATION_RANGE
*Type:* VARIABLE
Dsp pan attenuation range.

### DSP_PAN_OVERRIDE_RANGE
*Type:* VARIABLE
Dsp pan override range.

### DSP_THREE_EQ_CROSSOVERSLOPE_12DB
*Type:* VARIABLE
Dsp three eq crossoverslope 12db.

### DSP_THREE_EQ_CROSSOVERSLOPE_24DB
*Type:* VARIABLE
Dsp three eq crossoverslope 24db.

### DSP_THREE_EQ_CROSSOVERSLOPE_48DB
*Type:* VARIABLE
Dsp three eq crossoverslope 48db.

### DSP_THREE_EQ_LOWGAIN
*Type:* VARIABLE
Dsp three eq lowgain.

### DSP_THREE_EQ_MIDGAIN
*Type:* VARIABLE
Dsp three eq midgain.

### DSP_THREE_EQ_HIGHGAIN
*Type:* VARIABLE
Dsp three eq highgain.

### DSP_THREE_EQ_LOWCROSSOVER
*Type:* VARIABLE
Dsp three eq lowcrossover.

### DSP_THREE_EQ_HIGHCROSSOVER
*Type:* VARIABLE
Dsp three eq highcrossover.

### DSP_THREE_EQ_CROSSOVERSLOPE
*Type:* VARIABLE
Dsp three eq crossoverslope.

### DSP_FFT_WINDOW_RECT
*Type:* VARIABLE
Dsp fft window rect.

### DSP_FFT_WINDOW_TRIANGLE
*Type:* VARIABLE
Dsp fft window triangle.

### DSP_FFT_WINDOW_HAMMING
*Type:* VARIABLE
Dsp fft window hamming.

### DSP_FFT_WINDOW_HANNING
*Type:* VARIABLE
Dsp fft window hanning.

### DSP_FFT_WINDOW_BLACKMAN
*Type:* VARIABLE
Dsp fft window blackman.

### DSP_FFT_WINDOW_BLACKMANHARRIS
*Type:* VARIABLE
Dsp fft window blackmanharris.

### DSP_FFT_DOWNMIX_NONE
*Type:* VARIABLE
Dsp fft downmix none.

### DSP_FFT_DOWNMIX_MONO
*Type:* VARIABLE
Dsp fft downmix mono.

### DSP_FFT_WINDOWSIZE
*Type:* VARIABLE
Dsp fft windowsize.

### DSP_FFT_WINDOW
*Type:* VARIABLE
Dsp fft window.

### DSP_FFT_BAND_START_FREQ
*Type:* VARIABLE
Dsp fft band start freq.

### DSP_FFT_BAND_STOP_FREQ
*Type:* VARIABLE
Dsp fft band stop freq.

### DSP_FFT_SPECTRUMDATA
*Type:* VARIABLE
Dsp fft spectrumdata.

### DSP_FFT_RMS
*Type:* VARIABLE
Dsp fft rms.

### DSP_FFT_SPECTRAL_CENTROID
*Type:* VARIABLE
Dsp fft spectral centroid.

### DSP_FFT_IMMEDIATE_MODE
*Type:* VARIABLE
Dsp fft immediate mode.

### DSP_FFT_DOWNMIX
*Type:* VARIABLE
Dsp fft downmix.

### DSP_FFT_CHANNEL
*Type:* VARIABLE
Dsp fft channel.

### DSP_LOUDNESS_METER_STATE
*Type:* VARIABLE
Dsp loudness meter state.

### DSP_LOUDNESS_METER_WEIGHTING
*Type:* VARIABLE
Dsp loudness meter weighting.

### DSP_LOUDNESS_METER_INFO
*Type:* VARIABLE
Dsp loudness meter info.

### DSP_LOUDNESS_METER_STATE_RESET_INTEGRATED
*Type:* VARIABLE
Dsp loudness meter state reset integrated.

### DSP_LOUDNESS_METER_STATE_RESET_MAXPEAK
*Type:* VARIABLE
Dsp loudness meter state reset maxpeak.

### DSP_LOUDNESS_METER_STATE_RESET_ALL
*Type:* VARIABLE
Dsp loudness meter state reset all.

### DSP_LOUDNESS_METER_STATE_PAUSED
*Type:* VARIABLE
Dsp loudness meter state paused.

### DSP_LOUDNESS_METER_STATE_ANALYZING
*Type:* VARIABLE
Dsp loudness meter state analyzing.

### DSP_CONVOLUTION_REVERB_PARAM_IR
*Type:* VARIABLE
Dsp convolution reverb param ir.

### DSP_CONVOLUTION_REVERB_PARAM_WET
*Type:* VARIABLE
Dsp convolution reverb param wet.

### DSP_CONVOLUTION_REVERB_PARAM_DRY
*Type:* VARIABLE
Dsp convolution reverb param dry.

### DSP_CONVOLUTION_REVERB_PARAM_LINKED
*Type:* VARIABLE
Dsp convolution reverb param linked.

### DSP_CHANNELMIX_OUTPUT_DEFAULT
*Type:* VARIABLE
Dsp channelmix output default.

### DSP_CHANNELMIX_OUTPUT_ALLMONO
*Type:* VARIABLE
Dsp channelmix output allmono.

### DSP_CHANNELMIX_OUTPUT_ALLSTEREO
*Type:* VARIABLE
Dsp channelmix output allstereo.

### DSP_CHANNELMIX_OUTPUT_ALLQUAD
*Type:* VARIABLE
Dsp channelmix output allquad.

### DSP_CHANNELMIX_OUTPUT_ALL5POINT1
*Type:* VARIABLE
Dsp channelmix output all5point1.

### DSP_CHANNELMIX_OUTPUT_ALL7POINT1
*Type:* VARIABLE
Dsp channelmix output all7point1.

### DSP_CHANNELMIX_OUTPUT_ALLLFE
*Type:* VARIABLE
Dsp channelmix output alllfe.

### DSP_CHANNELMIX_OUTPUT_ALL7POINT1POINT4
*Type:* VARIABLE
Dsp channelmix output all7point1point4.

### DSP_CHANNELMIX_OUTPUTGROUPING
*Type:* VARIABLE
Dsp channelmix outputgrouping.

### DSP_CHANNELMIX_GAIN_CH0
*Type:* VARIABLE
Dsp channelmix gain ch0.

### DSP_CHANNELMIX_GAIN_CH1
*Type:* VARIABLE
Dsp channelmix gain ch1.

### DSP_CHANNELMIX_GAIN_CH2
*Type:* VARIABLE
Dsp channelmix gain ch2.

### DSP_CHANNELMIX_GAIN_CH3
*Type:* VARIABLE
Dsp channelmix gain ch3.

### DSP_CHANNELMIX_GAIN_CH4
*Type:* VARIABLE
Dsp channelmix gain ch4.

### DSP_CHANNELMIX_GAIN_CH5
*Type:* VARIABLE
Dsp channelmix gain ch5.

### DSP_CHANNELMIX_GAIN_CH6
*Type:* VARIABLE
Dsp channelmix gain ch6.

### DSP_CHANNELMIX_GAIN_CH7
*Type:* VARIABLE
Dsp channelmix gain ch7.

### DSP_CHANNELMIX_GAIN_CH8
*Type:* VARIABLE
Dsp channelmix gain ch8.

### DSP_CHANNELMIX_GAIN_CH9
*Type:* VARIABLE
Dsp channelmix gain ch9.

### DSP_CHANNELMIX_GAIN_CH10
*Type:* VARIABLE
Dsp channelmix gain ch10.

### DSP_CHANNELMIX_GAIN_CH11
*Type:* VARIABLE
Dsp channelmix gain ch11.

### DSP_CHANNELMIX_GAIN_CH12
*Type:* VARIABLE
Dsp channelmix gain ch12.

### DSP_CHANNELMIX_GAIN_CH13
*Type:* VARIABLE
Dsp channelmix gain ch13.

### DSP_CHANNELMIX_GAIN_CH14
*Type:* VARIABLE
Dsp channelmix gain ch14.

### DSP_CHANNELMIX_GAIN_CH15
*Type:* VARIABLE
Dsp channelmix gain ch15.

### DSP_CHANNELMIX_GAIN_CH16
*Type:* VARIABLE
Dsp channelmix gain ch16.

### DSP_CHANNELMIX_GAIN_CH17
*Type:* VARIABLE
Dsp channelmix gain ch17.

### DSP_CHANNELMIX_GAIN_CH18
*Type:* VARIABLE
Dsp channelmix gain ch18.

### DSP_CHANNELMIX_GAIN_CH19
*Type:* VARIABLE
Dsp channelmix gain ch19.

### DSP_CHANNELMIX_GAIN_CH20
*Type:* VARIABLE
Dsp channelmix gain ch20.

### DSP_CHANNELMIX_GAIN_CH21
*Type:* VARIABLE
Dsp channelmix gain ch21.

### DSP_CHANNELMIX_GAIN_CH22
*Type:* VARIABLE
Dsp channelmix gain ch22.

### DSP_CHANNELMIX_GAIN_CH23
*Type:* VARIABLE
Dsp channelmix gain ch23.

### DSP_CHANNELMIX_GAIN_CH24
*Type:* VARIABLE
Dsp channelmix gain ch24.

### DSP_CHANNELMIX_GAIN_CH25
*Type:* VARIABLE
Dsp channelmix gain ch25.

### DSP_CHANNELMIX_GAIN_CH26
*Type:* VARIABLE
Dsp channelmix gain ch26.

### DSP_CHANNELMIX_GAIN_CH27
*Type:* VARIABLE
Dsp channelmix gain ch27.

### DSP_CHANNELMIX_GAIN_CH28
*Type:* VARIABLE
Dsp channelmix gain ch28.

### DSP_CHANNELMIX_GAIN_CH29
*Type:* VARIABLE
Dsp channelmix gain ch29.

### DSP_CHANNELMIX_GAIN_CH30
*Type:* VARIABLE
Dsp channelmix gain ch30.

### DSP_CHANNELMIX_GAIN_CH31
*Type:* VARIABLE
Dsp channelmix gain ch31.

### DSP_CHANNELMIX_OUTPUT_CH0
*Type:* VARIABLE
Dsp channelmix output ch0.

### DSP_CHANNELMIX_OUTPUT_CH1
*Type:* VARIABLE
Dsp channelmix output ch1.

### DSP_CHANNELMIX_OUTPUT_CH2
*Type:* VARIABLE
Dsp channelmix output ch2.

### DSP_CHANNELMIX_OUTPUT_CH3
*Type:* VARIABLE
Dsp channelmix output ch3.

### DSP_CHANNELMIX_OUTPUT_CH4
*Type:* VARIABLE
Dsp channelmix output ch4.

### DSP_CHANNELMIX_OUTPUT_CH5
*Type:* VARIABLE
Dsp channelmix output ch5.

### DSP_CHANNELMIX_OUTPUT_CH6
*Type:* VARIABLE
Dsp channelmix output ch6.

### DSP_CHANNELMIX_OUTPUT_CH7
*Type:* VARIABLE
Dsp channelmix output ch7.

### DSP_CHANNELMIX_OUTPUT_CH8
*Type:* VARIABLE
Dsp channelmix output ch8.

### DSP_CHANNELMIX_OUTPUT_CH9
*Type:* VARIABLE
Dsp channelmix output ch9.

### DSP_CHANNELMIX_OUTPUT_CH10
*Type:* VARIABLE
Dsp channelmix output ch10.

### DSP_CHANNELMIX_OUTPUT_CH11
*Type:* VARIABLE
Dsp channelmix output ch11.

### DSP_CHANNELMIX_OUTPUT_CH12
*Type:* VARIABLE
Dsp channelmix output ch12.

### DSP_CHANNELMIX_OUTPUT_CH13
*Type:* VARIABLE
Dsp channelmix output ch13.

### DSP_CHANNELMIX_OUTPUT_CH14
*Type:* VARIABLE
Dsp channelmix output ch14.

### DSP_CHANNELMIX_OUTPUT_CH15
*Type:* VARIABLE
Dsp channelmix output ch15.

### DSP_CHANNELMIX_OUTPUT_CH16
*Type:* VARIABLE
Dsp channelmix output ch16.

### DSP_CHANNELMIX_OUTPUT_CH17
*Type:* VARIABLE
Dsp channelmix output ch17.

### DSP_CHANNELMIX_OUTPUT_CH18
*Type:* VARIABLE
Dsp channelmix output ch18.

### DSP_CHANNELMIX_OUTPUT_CH19
*Type:* VARIABLE
Dsp channelmix output ch19.

### DSP_CHANNELMIX_OUTPUT_CH20
*Type:* VARIABLE
Dsp channelmix output ch20.

### DSP_CHANNELMIX_OUTPUT_CH21
*Type:* VARIABLE
Dsp channelmix output ch21.

### DSP_CHANNELMIX_OUTPUT_CH22
*Type:* VARIABLE
Dsp channelmix output ch22.

### DSP_CHANNELMIX_OUTPUT_CH23
*Type:* VARIABLE
Dsp channelmix output ch23.

### DSP_CHANNELMIX_OUTPUT_CH24
*Type:* VARIABLE
Dsp channelmix output ch24.

### DSP_CHANNELMIX_OUTPUT_CH25
*Type:* VARIABLE
Dsp channelmix output ch25.

### DSP_CHANNELMIX_OUTPUT_CH26
*Type:* VARIABLE
Dsp channelmix output ch26.

### DSP_CHANNELMIX_OUTPUT_CH27
*Type:* VARIABLE
Dsp channelmix output ch27.

### DSP_CHANNELMIX_OUTPUT_CH28
*Type:* VARIABLE
Dsp channelmix output ch28.

### DSP_CHANNELMIX_OUTPUT_CH29
*Type:* VARIABLE
Dsp channelmix output ch29.

### DSP_CHANNELMIX_OUTPUT_CH30
*Type:* VARIABLE
Dsp channelmix output ch30.

### DSP_CHANNELMIX_OUTPUT_CH31
*Type:* VARIABLE
Dsp channelmix output ch31.

### DSP_TRANSCEIVER_SPEAKERMODE_AUTO
*Type:* VARIABLE
Dsp transceiver speakermode auto.

### DSP_TRANSCEIVER_SPEAKERMODE_MONO
*Type:* VARIABLE
Dsp transceiver speakermode mono.

### DSP_TRANSCEIVER_SPEAKERMODE_STEREO
*Type:* VARIABLE
Dsp transceiver speakermode stereo.

### DSP_TRANSCEIVER_SPEAKERMODE_SURROUND
*Type:* VARIABLE
Dsp transceiver speakermode surround.

### DSP_TRANSCEIVER_TRANSMIT
*Type:* VARIABLE
Dsp transceiver transmit.

### DSP_TRANSCEIVER_GAIN
*Type:* VARIABLE
Dsp transceiver gain.

### DSP_TRANSCEIVER_CHANNEL
*Type:* VARIABLE
Dsp transceiver channel.

### DSP_TRANSCEIVER_TRANSMITSPEAKERMODE
*Type:* VARIABLE
Dsp transceiver transmitspeakermode.

### DSP_OBJECTPAN_3D_POSITION
*Type:* VARIABLE
Dsp objectpan 3d position.

### DSP_OBJECTPAN_3D_ROLLOFF
*Type:* VARIABLE
Dsp objectpan 3d rolloff.

### DSP_OBJECTPAN_3D_MIN_DISTANCE
*Type:* VARIABLE
Dsp objectpan 3d min distance.

### DSP_OBJECTPAN_3D_MAX_DISTANCE
*Type:* VARIABLE
Dsp objectpan 3d max distance.

### DSP_OBJECTPAN_3D_EXTENT_MODE
*Type:* VARIABLE
Dsp objectpan 3d extent mode.

### DSP_OBJECTPAN_3D_SOUND_SIZE
*Type:* VARIABLE
Dsp objectpan 3d sound size.

### DSP_OBJECTPAN_3D_MIN_EXTENT
*Type:* VARIABLE
Dsp objectpan 3d min extent.

### DSP_OBJECTPAN_OVERALL_GAIN
*Type:* VARIABLE
Dsp objectpan overall gain.

### DSP_OBJECTPAN_OUTPUTGAIN
*Type:* VARIABLE
Dsp objectpan outputgain.

### DSP_OBJECTPAN_ATTENUATION_RANGE
*Type:* VARIABLE
Dsp objectpan attenuation range.

### DSP_OBJECTPAN_OVERRIDE_RANGE
*Type:* VARIABLE
Dsp objectpan override range.

### DSP_PROCESS_PERFORM
*Type:* VARIABLE
Dsp process perform.

### DSP_PROCESS_QUERY
*Type:* VARIABLE
Dsp process query.

### DSP_PAN_SURROUND_DEFAULT
*Type:* VARIABLE
Pan surround mode - default.

### DSP_PAN_SURROUND_ROTATION_NOT_BIASED
*Type:* VARIABLE
Pan surround mode - rotation not biased.

### DSP_PARAMETER_TYPE_FLOAT
*Type:* VARIABLE
DSP parameter type - float.

### DSP_PARAMETER_TYPE_INT
*Type:* VARIABLE
DSP parameter type - int.

### DSP_PARAMETER_TYPE_BOOL
*Type:* VARIABLE
DSP parameter type - bool.

### DSP_PARAMETER_TYPE_DATA
*Type:* VARIABLE
DSP parameter type - data.

### DSP_PARAMETER_FLOAT_MAPPING_TYPE_LINEAR
*Type:* VARIABLE
Dsp parameter float mapping type linear.

### DSP_PARAMETER_FLOAT_MAPPING_TYPE_AUTO
*Type:* VARIABLE
Dsp parameter float mapping type auto.

### DSP_PARAMETER_FLOAT_MAPPING_TYPE_PIECEWISE_LINEAR
*Type:* VARIABLE
Dsp parameter float mapping type piecewise linear.

### DSP_PARAMETER_DATA_TYPE_USER
*Type:* VARIABLE
Dsp parameter data type user.

### DSP_PARAMETER_DATA_TYPE_OVERALLGAIN
*Type:* VARIABLE
Dsp parameter data type overallgain.

### DSP_PARAMETER_DATA_TYPE_3DATTRIBUTES
*Type:* VARIABLE
Dsp parameter data type 3dattributes.

### DSP_PARAMETER_DATA_TYPE_SIDECHAIN
*Type:* VARIABLE
Dsp parameter data type sidechain.

### DSP_PARAMETER_DATA_TYPE_FFT
*Type:* VARIABLE
Dsp parameter data type fft.

### DSP_PARAMETER_DATA_TYPE_3DATTRIBUTES_MULTI
*Type:* VARIABLE
Dsp parameter data type 3dattributes multi.

### DSP_PARAMETER_DATA_TYPE_ATTENUATION_RANGE
*Type:* VARIABLE
Dsp parameter data type attenuation range.

### DSP_PARAMETER_DATA_TYPE_DYNAMIC_RESPONSE
*Type:* VARIABLE
Dsp parameter data type dynamic response.

### STUDIO_LOADING_STATE_UNLOADING
*Type:* VARIABLE
Loading state - unloading.

### STUDIO_LOADING_STATE_UNLOADED
*Type:* VARIABLE
Loading state - unloaded.

### STUDIO_LOADING_STATE_LOADING
*Type:* VARIABLE
Loading state - loading.

### STUDIO_LOADING_STATE_LOADED
*Type:* VARIABLE
Loading state - loaded.

### STUDIO_LOADING_STATE_ERROR
*Type:* VARIABLE
Loading state - error.

### STUDIO_LOAD_MEMORY
*Type:* VARIABLE
Studio load memory.

### STUDIO_LOAD_MEMORY_POINT
*Type:* VARIABLE
Studio load memory point.

### STUDIO_PARAMETER_GAME_CONTROLLED
*Type:* VARIABLE
Studio parameter type - game controlled.

### STUDIO_PARAMETER_AUTOMATIC_DISTANCE
*Type:* VARIABLE
Studio parameter type - automatic distance.

### STUDIO_PARAMETER_AUTOMATIC_EVENT_CONE_ANGLE
*Type:* VARIABLE
Studio parameter type - automatic event cone angle.

### STUDIO_PARAMETER_AUTOMATIC_EVENT_ORIENTATION
*Type:* VARIABLE
Studio parameter type - automatic event orientation.

### STUDIO_PARAMETER_AUTOMATIC_DIRECTION
*Type:* VARIABLE
Studio parameter type - automatic direction.

### STUDIO_PARAMETER_AUTOMATIC_ELEVATION
*Type:* VARIABLE
Studio parameter type - automatic elevation.

### STUDIO_PARAMETER_AUTOMATIC_LISTENER_ORIENTATION
*Type:* VARIABLE
Studio parameter type - automatic listener orientation.

### STUDIO_PARAMETER_AUTOMATIC_SPEED
*Type:* VARIABLE
Studio parameter type - automatic speed.

### STUDIO_PARAMETER_AUTOMATIC_SPEED_ABSOLUTE
*Type:* VARIABLE
Studio parameter type - automatic speed absolute.

### STUDIO_PARAMETER_AUTOMATIC_DISTANCE_NORMALIZED
*Type:* VARIABLE
Studio parameter type - automatic distance normalized.

### STUDIO_USER_PROPERTY_TYPE_INTEGER
*Type:* VARIABLE
User property type - integer.

### STUDIO_USER_PROPERTY_TYPE_BOOLEAN
*Type:* VARIABLE
User property type - boolean.

### STUDIO_USER_PROPERTY_TYPE_FLOAT
*Type:* VARIABLE
User property type - float.

### STUDIO_USER_PROPERTY_TYPE_STRING
*Type:* VARIABLE
User property type - string.

### STUDIO_EVENT_PROPERTY_CHANNELPRIORITY
*Type:* VARIABLE
Event property - channelpriority.

### STUDIO_EVENT_PROPERTY_SCHEDULE_DELAY
*Type:* VARIABLE
Event property - schedule delay.

### STUDIO_EVENT_PROPERTY_SCHEDULE_LOOKAHEAD
*Type:* VARIABLE
Event property - schedule lookahead.

### STUDIO_EVENT_PROPERTY_MINIMUM_DISTANCE
*Type:* VARIABLE
Event property - minimum distance.

### STUDIO_EVENT_PROPERTY_MAXIMUM_DISTANCE
*Type:* VARIABLE
Event property - maximum distance.

### STUDIO_EVENT_PROPERTY_COOLDOWN
*Type:* VARIABLE
Event property - cooldown.

### STUDIO_PLAYBACK_PLAYING
*Type:* VARIABLE
Playback state - playing.

### STUDIO_PLAYBACK_SUSTAINING
*Type:* VARIABLE
Playback state - sustaining.

### STUDIO_PLAYBACK_STOPPED
*Type:* VARIABLE
Playback state - stopped.

### STUDIO_PLAYBACK_STARTING
*Type:* VARIABLE
Playback state - starting.

### STUDIO_PLAYBACK_STOPPING
*Type:* VARIABLE
Playback state - stopping.

### STUDIO_STOP_ALLOWFADEOUT
*Type:* VARIABLE
Stop mode - allowfadeout.

### STUDIO_STOP_IMMEDIATE
*Type:* VARIABLE
Stop mode - immediate.

### STUDIO_INSTANCETYPE_NONE
*Type:* VARIABLE
Instance type - none.

### STUDIO_INSTANCETYPE_SYSTEM
*Type:* VARIABLE
Instance type - system.

### STUDIO_INSTANCETYPE_EVENTDESCRIPTION
*Type:* VARIABLE
Instance type - eventdescription.

### STUDIO_INSTANCETYPE_EVENTINSTANCE
*Type:* VARIABLE
Instance type - eventinstance.

### STUDIO_INSTANCETYPE_PARAMETERINSTANCE
*Type:* VARIABLE
Instance type - parameterinstance.

### STUDIO_INSTANCETYPE_BUS
*Type:* VARIABLE
Instance type - bus.

### STUDIO_INSTANCETYPE_VCA
*Type:* VARIABLE
Instance type - vca.

### STUDIO_INSTANCETYPE_BANK
*Type:* VARIABLE
Instance type - bank.

### STUDIO_INSTANCETYPE_COMMANDREPLAY
*Type:* VARIABLE
Instance type - commandreplay.

### VERSION
*Type:* VARIABLE
Version.

### BUILDNUMBER
*Type:* VARIABLE
Buildnumber.

### DEBUG_LEVEL_NONE
*Type:* VARIABLE
Debug level none.

### DEBUG_LEVEL_ERROR
*Type:* VARIABLE
Debug level error.

### DEBUG_LEVEL_WARNING
*Type:* VARIABLE
Debug level warning.

### DEBUG_LEVEL_LOG
*Type:* VARIABLE
Debug level log.

### DEBUG_TYPE_MEMORY
*Type:* VARIABLE
Debug type memory.

### DEBUG_TYPE_FILE
*Type:* VARIABLE
Debug type file.

### DEBUG_TYPE_CODEC
*Type:* VARIABLE
Debug type codec.

### DEBUG_TYPE_TRACE
*Type:* VARIABLE
Debug type trace.

### DEBUG_TYPE_VIRTUAL
*Type:* VARIABLE
Debug type virtual.

### DEBUG_DISPLAY_TIMESTAMPS
*Type:* VARIABLE
Debug display timestamps.

### DEBUG_DISPLAY_LINENUMBERS
*Type:* VARIABLE
Debug display linenumbers.

### DEBUG_DISPLAY_THREAD
*Type:* VARIABLE
Debug display thread.

### MEMORY_NORMAL
*Type:* VARIABLE
Memory normal.

### MEMORY_STREAM_FILE
*Type:* VARIABLE
Memory stream file.

### MEMORY_STREAM_DECODE
*Type:* VARIABLE
Memory stream decode.

### MEMORY_SAMPLEDATA
*Type:* VARIABLE
Memory sampledata.

### MEMORY_DSP_BUFFER
*Type:* VARIABLE
Memory dsp buffer.

### MEMORY_PLUGIN
*Type:* VARIABLE
Memory plugin.

### MEMORY_PERSISTENT
*Type:* VARIABLE
Memory persistent.

### MEMORY_ALL
*Type:* VARIABLE
Memory all.

### INIT_NORMAL
*Type:* VARIABLE
Init normal.

### INIT_STREAM_FROM_UPDATE
*Type:* VARIABLE
Init stream from update.

### INIT_MIX_FROM_UPDATE
*Type:* VARIABLE
Init mix from update.

### INIT_3D_RIGHTHANDED
*Type:* VARIABLE
Init 3d righthanded.

### INIT_CLIP_OUTPUT
*Type:* VARIABLE
Init clip output.

### INIT_CHANNEL_LOWPASS
*Type:* VARIABLE
Init channel lowpass.

### INIT_CHANNEL_DISTANCEFILTER
*Type:* VARIABLE
Init channel distancefilter.

### INIT_PROFILE_ENABLE
*Type:* VARIABLE
Init profile enable.

### INIT_VOL0_BECOMES_VIRTUAL
*Type:* VARIABLE
Init vol0 becomes virtual.

### INIT_GEOMETRY_USECLOSEST
*Type:* VARIABLE
Init geometry useclosest.

### INIT_PREFER_DOLBY_DOWNMIX
*Type:* VARIABLE
Init prefer dolby downmix.

### INIT_THREAD_UNSAFE
*Type:* VARIABLE
Init thread unsafe.

### INIT_PROFILE_METER_ALL
*Type:* VARIABLE
Init profile meter all.

### INIT_MEMORY_TRACKING
*Type:* VARIABLE
Init memory tracking.

### DRIVER_STATE_CONNECTED
*Type:* VARIABLE
Driver state - connected.

### DRIVER_STATE_DEFAULT
*Type:* VARIABLE
Driver state - default.

### TIMEUNIT_MS
*Type:* VARIABLE
Time unit - ms.

### TIMEUNIT_PCM
*Type:* VARIABLE
Time unit - pcm.

### TIMEUNIT_PCMBYTES
*Type:* VARIABLE
Time unit - pcmbytes.

### TIMEUNIT_RAWBYTES
*Type:* VARIABLE
Time unit - rawbytes.

### TIMEUNIT_PCMFRACTION
*Type:* VARIABLE
Time unit - pcmfraction.

### TIMEUNIT_MODORDER
*Type:* VARIABLE
Time unit - modorder.

### TIMEUNIT_MODROW
*Type:* VARIABLE
Time unit - modrow.

### TIMEUNIT_MODPATTERN
*Type:* VARIABLE
Time unit - modpattern.

### SYSTEM_CALLBACK_DEVICELISTCHANGED
*Type:* VARIABLE
System callback devicelistchanged.

### SYSTEM_CALLBACK_DEVICELOST
*Type:* VARIABLE
System callback devicelost.

### SYSTEM_CALLBACK_MEMORYALLOCATIONFAILED
*Type:* VARIABLE
System callback memoryallocationfailed.

### SYSTEM_CALLBACK_THREADCREATED
*Type:* VARIABLE
System callback threadcreated.

### SYSTEM_CALLBACK_BADDSPCONNECTION
*Type:* VARIABLE
System callback baddspconnection.

### SYSTEM_CALLBACK_PREMIX
*Type:* VARIABLE
System callback premix.

### SYSTEM_CALLBACK_POSTMIX
*Type:* VARIABLE
System callback postmix.

### SYSTEM_CALLBACK_ERROR
*Type:* VARIABLE
System callback error.

### SYSTEM_CALLBACK_THREADDESTROYED
*Type:* VARIABLE
System callback threaddestroyed.

### SYSTEM_CALLBACK_PREUPDATE
*Type:* VARIABLE
System callback preupdate.

### SYSTEM_CALLBACK_POSTUPDATE
*Type:* VARIABLE
System callback postupdate.

### SYSTEM_CALLBACK_RECORDLISTCHANGED
*Type:* VARIABLE
System callback recordlistchanged.

### SYSTEM_CALLBACK_BUFFEREDNOMIX
*Type:* VARIABLE
System callback bufferednomix.

### SYSTEM_CALLBACK_DEVICEREINITIALIZE
*Type:* VARIABLE
System callback devicereinitialize.

### SYSTEM_CALLBACK_OUTPUTUNDERRUN
*Type:* VARIABLE
System callback outputunderrun.

### SYSTEM_CALLBACK_RECORDPOSITIONCHANGED
*Type:* VARIABLE
System callback recordpositionchanged.

### SYSTEM_CALLBACK_ALL
*Type:* VARIABLE
System callback all.

### DEFAULT
*Type:* VARIABLE
Default.

### LOOP_OFF
*Type:* VARIABLE
Loop off.

### LOOP_NORMAL
*Type:* VARIABLE
Loop normal.

### LOOP_BIDI
*Type:* VARIABLE
Loop bidi.

### 2D
*Type:* VARIABLE
2d.

### 3D
*Type:* VARIABLE
3d.

### CREATESTREAM
*Type:* VARIABLE
Createstream.

### CREATESAMPLE
*Type:* VARIABLE
Createsample.

### CREATECOMPRESSEDSAMPLE
*Type:* VARIABLE
Createcompressedsample.

### OPENUSER
*Type:* VARIABLE
Openuser.

### OPENMEMORY
*Type:* VARIABLE
Openmemory.

### OPENMEMORY_POINT
*Type:* VARIABLE
Openmemory point.

### OPENRAW
*Type:* VARIABLE
Openraw.

### OPENONLY
*Type:* VARIABLE
Openonly.

### ACCURATETIME
*Type:* VARIABLE
Accuratetime.

### MPEGSEARCH
*Type:* VARIABLE
Mpegsearch.

### NONBLOCKING
*Type:* VARIABLE
Nonblocking.

### UNIQUE
*Type:* VARIABLE
Unique.

### 3D_HEADRELATIVE
*Type:* VARIABLE
3d headrelative.

### 3D_WORLDRELATIVE
*Type:* VARIABLE
3d worldrelative.

### 3D_INVERSEROLLOFF
*Type:* VARIABLE
3d inverserolloff.

### 3D_LINEARROLLOFF
*Type:* VARIABLE
3d linearrolloff.

### 3D_LINEARSQUAREROLLOFF
*Type:* VARIABLE
3d linearsquarerolloff.

### 3D_INVERSETAPEREDROLLOFF
*Type:* VARIABLE
3d inversetaperedrolloff.

### 3D_CUSTOMROLLOFF
*Type:* VARIABLE
3d customrolloff.

### 3D_IGNOREGEOMETRY
*Type:* VARIABLE
3d ignoregeometry.

### IGNORETAGS
*Type:* VARIABLE
Ignoretags.

### LOWMEM
*Type:* VARIABLE
Lowmem.

### VIRTUAL_PLAYFROMSTART
*Type:* VARIABLE
Virtual playfromstart.

### CHANNELMASK_FRONT_LEFT
*Type:* VARIABLE
Channelmask front left.

### CHANNELMASK_FRONT_RIGHT
*Type:* VARIABLE
Channelmask front right.

### CHANNELMASK_FRONT_CENTER
*Type:* VARIABLE
Channelmask front center.

### CHANNELMASK_LOW_FREQUENCY
*Type:* VARIABLE
Channelmask low frequency.

### CHANNELMASK_SURROUND_LEFT
*Type:* VARIABLE
Channelmask surround left.

### CHANNELMASK_SURROUND_RIGHT
*Type:* VARIABLE
Channelmask surround right.

### CHANNELMASK_BACK_LEFT
*Type:* VARIABLE
Channelmask back left.

### CHANNELMASK_BACK_RIGHT
*Type:* VARIABLE
Channelmask back right.

### CHANNELMASK_BACK_CENTER
*Type:* VARIABLE
Channelmask back center.

### CHANNELMASK_MONO
*Type:* VARIABLE
Channelmask mono.

### CHANNELMASK_STEREO
*Type:* VARIABLE
Channelmask stereo.

### CHANNELMASK_LRC
*Type:* VARIABLE
Channelmask lrc.

### CHANNELMASK_QUAD
*Type:* VARIABLE
Channelmask quad.

### CHANNELMASK_SURROUND
*Type:* VARIABLE
Channelmask surround.

### CHANNELMASK_5POINT1
*Type:* VARIABLE
Channelmask 5point1.

### CHANNELMASK_5POINT1_REARS
*Type:* VARIABLE
Channelmask 5point1 rears.

### CHANNELMASK_7POINT0
*Type:* VARIABLE
Channelmask 7point0.

### CHANNELMASK_7POINT1
*Type:* VARIABLE
Channelmask 7point1.

### PORT_INDEX_NONE
*Type:* VARIABLE
Port index none.

### THREAD_PRIORITY_PLATFORM_MIN
*Type:* VARIABLE
Thread priority - platform min.

### THREAD_PRIORITY_PLATFORM_MAX
*Type:* VARIABLE
Thread priority - platform max.

### THREAD_PRIORITY_DEFAULT
*Type:* VARIABLE
Thread priority - default.

### THREAD_PRIORITY_LOW
*Type:* VARIABLE
Thread priority - low.

### THREAD_PRIORITY_MEDIUM
*Type:* VARIABLE
Thread priority - medium.

### THREAD_PRIORITY_HIGH
*Type:* VARIABLE
Thread priority - high.

### THREAD_PRIORITY_VERY_HIGH
*Type:* VARIABLE
Thread priority - very high.

### THREAD_PRIORITY_EXTREME
*Type:* VARIABLE
Thread priority - extreme.

### THREAD_PRIORITY_CRITICAL
*Type:* VARIABLE
Thread priority - critical.

### THREAD_PRIORITY_MIXER
*Type:* VARIABLE
Thread priority - mixer.

### THREAD_PRIORITY_FEEDER
*Type:* VARIABLE
Thread priority - feeder.

### THREAD_PRIORITY_STREAM
*Type:* VARIABLE
Thread priority - stream.

### THREAD_PRIORITY_FILE
*Type:* VARIABLE
Thread priority - file.

### THREAD_PRIORITY_NONBLOCKING
*Type:* VARIABLE
Thread priority - nonblocking.

### THREAD_PRIORITY_RECORD
*Type:* VARIABLE
Thread priority - record.

### THREAD_PRIORITY_GEOMETRY
*Type:* VARIABLE
Thread priority - geometry.

### THREAD_PRIORITY_PROFILER
*Type:* VARIABLE
Thread priority - profiler.

### THREAD_PRIORITY_STUDIO_UPDATE
*Type:* VARIABLE
Thread priority - studio update.

### THREAD_PRIORITY_STUDIO_LOAD_BANK
*Type:* VARIABLE
Thread priority - studio load bank.

### THREAD_PRIORITY_STUDIO_LOAD_SAMPLE
*Type:* VARIABLE
Thread priority - studio load sample.

### THREAD_PRIORITY_CONVOLUTION1
*Type:* VARIABLE
Thread priority - convolution1.

### THREAD_PRIORITY_CONVOLUTION2
*Type:* VARIABLE
Thread priority - convolution2.

### THREAD_STACK_SIZE_DEFAULT
*Type:* VARIABLE
Thread stack size - default.

### THREAD_STACK_SIZE_MIXER
*Type:* VARIABLE
Thread stack size - mixer.

### THREAD_STACK_SIZE_FEEDER
*Type:* VARIABLE
Thread stack size - feeder.

### THREAD_STACK_SIZE_STREAM
*Type:* VARIABLE
Thread stack size - stream.

### THREAD_STACK_SIZE_FILE
*Type:* VARIABLE
Thread stack size - file.

### THREAD_STACK_SIZE_NONBLOCKING
*Type:* VARIABLE
Thread stack size - nonblocking.

### THREAD_STACK_SIZE_RECORD
*Type:* VARIABLE
Thread stack size - record.

### THREAD_STACK_SIZE_GEOMETRY
*Type:* VARIABLE
Thread stack size - geometry.

### THREAD_STACK_SIZE_PROFILER
*Type:* VARIABLE
Thread stack size - profiler.

### THREAD_STACK_SIZE_STUDIO_UPDATE
*Type:* VARIABLE
Thread stack size - studio update.

### THREAD_STACK_SIZE_STUDIO_LOAD_BANK
*Type:* VARIABLE
Thread stack size - studio load bank.

### THREAD_STACK_SIZE_STUDIO_LOAD_SAMPLE
*Type:* VARIABLE
Thread stack size - studio load sample.

### THREAD_STACK_SIZE_CONVOLUTION1
*Type:* VARIABLE
Thread stack size - convolution1.

### THREAD_STACK_SIZE_CONVOLUTION2
*Type:* VARIABLE
Thread stack size - convolution2.

### THREAD_AFFINITY_GROUP_DEFAULT
*Type:* VARIABLE
Thread affinity - group default.

### THREAD_AFFINITY_GROUP_A
*Type:* VARIABLE
Thread affinity - group a.

### THREAD_AFFINITY_GROUP_B
*Type:* VARIABLE
Thread affinity - group b.

### THREAD_AFFINITY_GROUP_C
*Type:* VARIABLE
Thread affinity - group c.

### THREAD_AFFINITY_MIXER
*Type:* VARIABLE
Thread affinity - mixer.

### THREAD_AFFINITY_FEEDER
*Type:* VARIABLE
Thread affinity - feeder.

### THREAD_AFFINITY_STREAM
*Type:* VARIABLE
Thread affinity - stream.

### THREAD_AFFINITY_FILE
*Type:* VARIABLE
Thread affinity - file.

### THREAD_AFFINITY_NONBLOCKING
*Type:* VARIABLE
Thread affinity - nonblocking.

### THREAD_AFFINITY_RECORD
*Type:* VARIABLE
Thread affinity - record.

### THREAD_AFFINITY_GEOMETRY
*Type:* VARIABLE
Thread affinity - geometry.

### THREAD_AFFINITY_PROFILER
*Type:* VARIABLE
Thread affinity - profiler.

### THREAD_AFFINITY_STUDIO_UPDATE
*Type:* VARIABLE
Thread affinity - studio update.

### THREAD_AFFINITY_STUDIO_LOAD_BANK
*Type:* VARIABLE
Thread affinity - studio load bank.

### THREAD_AFFINITY_STUDIO_LOAD_SAMPLE
*Type:* VARIABLE
Thread affinity - studio load sample.

### THREAD_AFFINITY_CONVOLUTION1
*Type:* VARIABLE
Thread affinity - convolution1.

### THREAD_AFFINITY_CONVOLUTION2
*Type:* VARIABLE
Thread affinity - convolution2.

### THREAD_AFFINITY_CORE_ALL
*Type:* VARIABLE
Thread affinity - core all.

### THREAD_AFFINITY_CORE_0
*Type:* VARIABLE
Thread affinity - core 0.

### THREAD_AFFINITY_CORE_1
*Type:* VARIABLE
Thread affinity - core 1.

### THREAD_AFFINITY_CORE_2
*Type:* VARIABLE
Thread affinity - core 2.

### THREAD_AFFINITY_CORE_3
*Type:* VARIABLE
Thread affinity - core 3.

### THREAD_AFFINITY_CORE_4
*Type:* VARIABLE
Thread affinity - core 4.

### THREAD_AFFINITY_CORE_5
*Type:* VARIABLE
Thread affinity - core 5.

### THREAD_AFFINITY_CORE_6
*Type:* VARIABLE
Thread affinity - core 6.

### THREAD_AFFINITY_CORE_7
*Type:* VARIABLE
Thread affinity - core 7.

### THREAD_AFFINITY_CORE_8
*Type:* VARIABLE
Thread affinity - core 8.

### THREAD_AFFINITY_CORE_9
*Type:* VARIABLE
Thread affinity - core 9.

### THREAD_AFFINITY_CORE_10
*Type:* VARIABLE
Thread affinity - core 10.

### THREAD_AFFINITY_CORE_11
*Type:* VARIABLE
Thread affinity - core 11.

### THREAD_AFFINITY_CORE_12
*Type:* VARIABLE
Thread affinity - core 12.

### THREAD_AFFINITY_CORE_13
*Type:* VARIABLE
Thread affinity - core 13.

### THREAD_AFFINITY_CORE_14
*Type:* VARIABLE
Thread affinity - core 14.

### THREAD_AFFINITY_CORE_15
*Type:* VARIABLE
Thread affinity - core 15.

### MAX_CHANNEL_WIDTH
*Type:* VARIABLE
Max channel width.

### MAX_SYSTEMS
*Type:* VARIABLE
Max systems.

### MAX_LISTENERS
*Type:* VARIABLE
Max listeners.

### REVERB_MAXINSTANCES
*Type:* VARIABLE
Reverb maxinstances.

### STUDIO_LOAD_MEMORY_ALIGNMENT
*Type:* VARIABLE
Studio load memory alignment.

### STUDIO_INIT_NORMAL
*Type:* VARIABLE
Studio init normal.

### STUDIO_INIT_LIVEUPDATE
*Type:* VARIABLE
Studio init liveupdate.

### STUDIO_INIT_ALLOW_MISSING_PLUGINS
*Type:* VARIABLE
Studio init allow missing plugins.

### STUDIO_INIT_SYNCHRONOUS_UPDATE
*Type:* VARIABLE
Studio init synchronous update.

### STUDIO_INIT_DEFERRED_CALLBACKS
*Type:* VARIABLE
Studio init deferred callbacks.

### STUDIO_INIT_LOAD_FROM_UPDATE
*Type:* VARIABLE
Studio init load from update.

### STUDIO_INIT_MEMORY_TRACKING
*Type:* VARIABLE
Studio init memory tracking.

### STUDIO_PARAMETER_READONLY
*Type:* VARIABLE
Studio parameter type - readonly.

### STUDIO_PARAMETER_AUTOMATIC
*Type:* VARIABLE
Studio parameter type - automatic.

### STUDIO_PARAMETER_GLOBAL
*Type:* VARIABLE
Studio parameter type - global.

### STUDIO_PARAMETER_DISCRETE
*Type:* VARIABLE
Studio parameter type - discrete.

### STUDIO_PARAMETER_LABELED
*Type:* VARIABLE
Studio parameter type - labeled.

### STUDIO_SYSTEM_CALLBACK_PREUPDATE
*Type:* VARIABLE
System callback type - preupdate.

### STUDIO_SYSTEM_CALLBACK_POSTUPDATE
*Type:* VARIABLE
System callback type - postupdate.

### STUDIO_SYSTEM_CALLBACK_BANK_UNLOAD
*Type:* VARIABLE
System callback type - bank unload.

### STUDIO_SYSTEM_CALLBACK_LIVEUPDATE_CONNECTED
*Type:* VARIABLE
System callback type - liveupdate connected.

### STUDIO_SYSTEM_CALLBACK_LIVEUPDATE_DISCONNECTED
*Type:* VARIABLE
System callback type - liveupdate disconnected.

### STUDIO_SYSTEM_CALLBACK_ALL
*Type:* VARIABLE
System callback type - all.

### STUDIO_EVENT_CALLBACK_CREATED
*Type:* VARIABLE
Event callback type - created.

### STUDIO_EVENT_CALLBACK_DESTROYED
*Type:* VARIABLE
Event callback type - destroyed.

### STUDIO_EVENT_CALLBACK_STARTING
*Type:* VARIABLE
Event callback type - starting.

### STUDIO_EVENT_CALLBACK_STARTED
*Type:* VARIABLE
Event callback type - started.

### STUDIO_EVENT_CALLBACK_RESTARTED
*Type:* VARIABLE
Event callback type - restarted.

### STUDIO_EVENT_CALLBACK_STOPPED
*Type:* VARIABLE
Event callback type - stopped.

### STUDIO_EVENT_CALLBACK_START_FAILED
*Type:* VARIABLE
Event callback type - start failed.

### STUDIO_EVENT_CALLBACK_CREATE_PROGRAMMER_SOUND
*Type:* VARIABLE
Event callback type - create programmer sound.

### STUDIO_EVENT_CALLBACK_DESTROY_PROGRAMMER_SOUND
*Type:* VARIABLE
Event callback type - destroy programmer sound.

### STUDIO_EVENT_CALLBACK_PLUGIN_CREATED
*Type:* VARIABLE
Event callback type - plugin created.

### STUDIO_EVENT_CALLBACK_PLUGIN_DESTROYED
*Type:* VARIABLE
Event callback type - plugin destroyed.

### STUDIO_EVENT_CALLBACK_TIMELINE_MARKER
*Type:* VARIABLE
Event callback type - timeline marker.

### STUDIO_EVENT_CALLBACK_TIMELINE_BEAT
*Type:* VARIABLE
Event callback type - timeline beat.

### STUDIO_EVENT_CALLBACK_SOUND_PLAYED
*Type:* VARIABLE
Event callback type - sound played.

### STUDIO_EVENT_CALLBACK_SOUND_STOPPED
*Type:* VARIABLE
Event callback type - sound stopped.

### STUDIO_EVENT_CALLBACK_REAL_TO_VIRTUAL
*Type:* VARIABLE
Event callback type - real to virtual.

### STUDIO_EVENT_CALLBACK_VIRTUAL_TO_REAL
*Type:* VARIABLE
Event callback type - virtual to real.

### STUDIO_EVENT_CALLBACK_START_EVENT_COMMAND
*Type:* VARIABLE
Event callback type - start event command.

### STUDIO_EVENT_CALLBACK_NESTED_TIMELINE_BEAT
*Type:* VARIABLE
Event callback type - nested timeline beat.

### STUDIO_EVENT_CALLBACK_ALL
*Type:* VARIABLE
Event callback type - all.

### STUDIO_LOAD_BANK_NORMAL
*Type:* VARIABLE
Bank loading mode - normal.

### STUDIO_LOAD_BANK_NONBLOCKING
*Type:* VARIABLE
Bank loading mode - nonblocking.

### STUDIO_LOAD_BANK_DECOMPRESS_SAMPLES
*Type:* VARIABLE
Bank loading mode - decompress samples.

### STUDIO_LOAD_BANK_UNENCRYPTED
*Type:* VARIABLE
Bank loading mode - unencrypted.

### STUDIO_COMMANDCAPTURE_NORMAL
*Type:* VARIABLE
Studio commandcapture normal.

### STUDIO_COMMANDCAPTURE_FILEFLUSH
*Type:* VARIABLE
Studio commandcapture fileflush.

### STUDIO_COMMANDCAPTURE_SKIP_INITIAL_STATE
*Type:* VARIABLE
Studio commandcapture skip initial state.

### STUDIO_COMMANDREPLAY_NORMAL
*Type:* VARIABLE
Studio commandreplay normal.

### STUDIO_COMMANDREPLAY_SKIP_CLEANUP
*Type:* VARIABLE
Studio commandreplay skip cleanup.

### STUDIO_COMMANDREPLAY_FAST_FORWARD
*Type:* VARIABLE
Studio commandreplay fast forward.

### STUDIO_COMMANDREPLAY_SKIP_BANK_LOAD
*Type:* VARIABLE
Studio commandreplay skip bank load.

### fmod.ASYNCREADINFO
*Type:* FUNCTION
Creates a new FMOD_ASYNCREADINFO struct

**Returns**

- `fmod.asyncreadinfo` - The created struct instance

### fmod._3D_ATTRIBUTES
*Type:* FUNCTION
Creates a new FMOD_3D_ATTRIBUTES struct

**Returns**

- `fmod.3d_attributes` - The created struct instance

### fmod.GUID
*Type:* FUNCTION
Creates a new FMOD_GUID struct

**Returns**

- `fmod.guid` - The created struct instance

### fmod.PLUGINLIST
*Type:* FUNCTION
Creates a new FMOD_PLUGINLIST struct

**Returns**

- `fmod.pluginlist` - The created struct instance

### fmod.ADVANCEDSETTINGS
*Type:* FUNCTION
Creates a new FMOD_ADVANCEDSETTINGS struct

**Returns**

- `fmod.advancedsettings` - The created struct instance

### fmod.TAG
*Type:* FUNCTION
Creates a new FMOD_TAG struct

**Returns**

- `fmod.tag` - The created struct instance

### fmod.CREATESOUNDEXINFO
*Type:* FUNCTION
Creates a new FMOD_CREATESOUNDEXINFO struct

**Returns**

- `fmod.createsoundexinfo` - The created struct instance

### fmod.REVERB_PROPERTIES
*Type:* FUNCTION
Creates a new FMOD_REVERB_PROPERTIES struct

**Returns**

- `fmod.reverb_properties` - The created struct instance

### fmod.ERRORCALLBACK_INFO
*Type:* FUNCTION
Creates a new FMOD_ERRORCALLBACK_INFO struct

**Returns**

- `fmod.errorcallback_info` - The created struct instance

### fmod.CPU_USAGE
*Type:* FUNCTION
Creates a new FMOD_CPU_USAGE struct

**Returns**

- `fmod.cpu_usage` - The created struct instance

### fmod.DSP_DATA_PARAMETER_INFO
*Type:* FUNCTION
Creates a new FMOD_DSP_DATA_PARAMETER_INFO struct

**Returns**

- `fmod.dsp_data_parameter_info` - The created struct instance

### fmod.CODEC_STATE
*Type:* FUNCTION
Creates a new FMOD_CODEC_STATE struct

**Returns**

- `fmod.codec_state` - The created struct instance

### fmod.CODEC_WAVEFORMAT
*Type:* FUNCTION
Creates a new FMOD_CODEC_WAVEFORMAT struct

**Returns**

- `fmod.codec_waveformat` - The created struct instance

### fmod.CODEC_DESCRIPTION
*Type:* FUNCTION
Creates a new FMOD_CODEC_DESCRIPTION struct

**Returns**

- `fmod.codec_description` - The created struct instance

### fmod.CODEC_STATE_FUNCTIONS
*Type:* FUNCTION
Creates a new FMOD_CODEC_STATE_FUNCTIONS struct

**Returns**

- `fmod.codec_state_functions` - The created struct instance

### fmod.DSP_LOUDNESS_METER_INFO_TYPE
*Type:* FUNCTION
Creates a new FMOD_DSP_LOUDNESS_METER_INFO_TYPE struct

**Returns**

- `fmod.dsp_loudness_meter_info_type` - The created struct instance

### fmod.DSP_LOUDNESS_METER_WEIGHTING_TYPE
*Type:* FUNCTION
Creates a new FMOD_DSP_LOUDNESS_METER_WEIGHTING_TYPE struct

**Returns**

- `fmod.dsp_loudness_meter_weighting_type` - The created struct instance

### fmod.DSP_STATE
*Type:* FUNCTION
Creates a new FMOD_DSP_STATE struct

**Returns**

- `fmod.dsp_state` - The created struct instance

### fmod.DSP_BUFFER_ARRAY
*Type:* FUNCTION
Creates a new FMOD_DSP_BUFFER_ARRAY struct

**Returns**

- `fmod.dsp_buffer_array` - The created struct instance

### fmod.COMPLEX
*Type:* FUNCTION
Creates a new FMOD_COMPLEX struct

**Returns**

- `fmod.complex` - The created struct instance

### fmod.DSP_PARAMETER_FLOAT_MAPPING_PIECEWISE_LINEAR
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_FLOAT_MAPPING_PIECEWISE_LINEAR struct

**Returns**

- `fmod.dsp_parameter_float_mapping_piecewise_linear` - The created struct instance

### fmod.DSP_PARAMETER_FLOAT_MAPPING
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_FLOAT_MAPPING struct

**Returns**

- `fmod.dsp_parameter_float_mapping` - The created struct instance

### fmod.DSP_PARAMETER_DESC_FLOAT
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_DESC_FLOAT struct

**Returns**

- `fmod.dsp_parameter_desc_float` - The created struct instance

### fmod.DSP_PARAMETER_DESC_INT
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_DESC_INT struct

**Returns**

- `fmod.dsp_parameter_desc_int` - The created struct instance

### fmod.DSP_PARAMETER_DESC_BOOL
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_DESC_BOOL struct

**Returns**

- `fmod.dsp_parameter_desc_bool` - The created struct instance

### fmod.DSP_PARAMETER_DESC_DATA
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_DESC_DATA struct

**Returns**

- `fmod.dsp_parameter_desc_data` - The created struct instance

### fmod.DSP_PARAMETER_DESC
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_DESC struct

**Returns**

- `fmod.dsp_parameter_desc` - The created struct instance

### fmod.DSP_PARAMETER_OVERALLGAIN
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_OVERALLGAIN struct

**Returns**

- `fmod.dsp_parameter_overallgain` - The created struct instance

### fmod.DSP_PARAMETER_3DATTRIBUTES
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_3DATTRIBUTES struct

**Returns**

- `fmod.dsp_parameter_3dattributes` - The created struct instance

### fmod.DSP_PARAMETER_3DATTRIBUTES_MULTI
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_3DATTRIBUTES_MULTI struct

**Returns**

- `fmod.dsp_parameter_3dattributes_multi` - The created struct instance

### fmod.DSP_PARAMETER_ATTENUATION_RANGE
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_ATTENUATION_RANGE struct

**Returns**

- `fmod.dsp_parameter_attenuation_range` - The created struct instance

### fmod.DSP_PARAMETER_SIDECHAIN
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_SIDECHAIN struct

**Returns**

- `fmod.dsp_parameter_sidechain` - The created struct instance

### fmod.DSP_PARAMETER_FFT
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_FFT struct

**Returns**

- `fmod.dsp_parameter_fft` - The created struct instance

### fmod.DSP_PARAMETER_DYNAMIC_RESPONSE
*Type:* FUNCTION
Creates a new FMOD_DSP_PARAMETER_DYNAMIC_RESPONSE struct

**Returns**

- `fmod.dsp_parameter_dynamic_response` - The created struct instance

### fmod.DSP_DESCRIPTION
*Type:* FUNCTION
Creates a new FMOD_DSP_DESCRIPTION struct

**Returns**

- `fmod.dsp_description` - The created struct instance

### fmod.DSP_STATE_DFT_FUNCTIONS
*Type:* FUNCTION
Creates a new FMOD_DSP_STATE_DFT_FUNCTIONS struct

**Returns**

- `fmod.dsp_state_dft_functions` - The created struct instance

### fmod.DSP_STATE_PAN_FUNCTIONS
*Type:* FUNCTION
Creates a new FMOD_DSP_STATE_PAN_FUNCTIONS struct

**Returns**

- `fmod.dsp_state_pan_functions` - The created struct instance

### fmod.DSP_STATE_FUNCTIONS
*Type:* FUNCTION
Creates a new FMOD_DSP_STATE_FUNCTIONS struct

**Returns**

- `fmod.dsp_state_functions` - The created struct instance

### fmod.DSP_METERING_INFO
*Type:* FUNCTION
Creates a new FMOD_DSP_METERING_INFO struct

**Returns**

- `fmod.dsp_metering_info` - The created struct instance

### fmod.OUTPUT_STATE
*Type:* FUNCTION
Creates a new FMOD_OUTPUT_STATE struct

**Returns**

- `fmod.output_state` - The created struct instance

### fmod.OUTPUT_OBJECT3DINFO
*Type:* FUNCTION
Creates a new FMOD_OUTPUT_OBJECT3DINFO struct

**Returns**

- `fmod.output_object3dinfo` - The created struct instance

### fmod.OUTPUT_DESCRIPTION
*Type:* FUNCTION
Creates a new FMOD_OUTPUT_DESCRIPTION struct

**Returns**

- `fmod.output_description` - The created struct instance

### fmod.memory_initialize
*Type:* FUNCTION
Initialize for memory.

### fmod.memory_get_stats
*Type:* FUNCTION
Get stats for memory.

**Parameters**

- `blocking` (boolean) - Bool value

**Returns**

- `userdata` - The currentalloced value
- `userdata` - The maxalloced value

### fmod.debug_initialize
*Type:* FUNCTION
Initialize for debug.

### fmod.file_set_disk_busy
*Type:* FUNCTION
Set disk busy for file.

**Parameters**

- `busy` (number) - Bus handle

### fmod.file_get_disk_busy
*Type:* FUNCTION
Get disk busy for file.

**Returns**

- `userdata` - The busy value

### fmod.thread_set_attributes
*Type:* FUNCTION
Set attributes for thread.

**Parameters**

- `type` (number) - Type value
- `affinity` (number) - Affinity value
- `priority` (number) - Priority (0 = highest, 256 = lowest)
- `stacksize` (number) - Size value

### fmod.system_create
*Type:* FUNCTION
Create for system.

**Parameters**

- `headerversion` (number) - headerversion

**Returns**

- `userdata` - The system value

### system
*Type:* FMOD.SYSTEM
The FMOD low-level system instance

###
*Type:* TABLE
Table mapping error messages to error codes

### fmod.s64
*Type:* FUNCTION
Creates a signed 64-bit integer value

**Parameters**

- `value` (number) - The value (or low 32 bits if high is provided)
- `high` (number) - The high 32 bits (optional)

**Returns**

- `userdata` - The 64-bit integer value

### fmod.u64
*Type:* FUNCTION
Creates an unsigned 64-bit integer value

**Parameters**

- `value` (number) - The value (or low 32 bits if high is provided)
- `high` (number) - The high 32 bits (optional)

**Returns**

- `userdata` - The 64-bit integer value
