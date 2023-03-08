<script>

    //TODO: Audio should all be in a giant array to iterate over.
    export let src;
    let audioFile = new Audio(src);
    let isPlaying = false;

    const icons = {
        play : "img/play.png",
        pause : "img/pause.png"
    }

    function playAudio()
    {
        if (audioFile.paused) {
            audioFile.play();
            isPlaying = true;
        } else {
            audioFile.pause();
            isPlaying = false;
        }
    }
</script>


<div class="audio-player">
    <button aria-roledescription="Play Audio" on:click={()=>playAudio()}>
        <img src="{isPlaying ? icons.pause : icons.play}" class="play-button" alt="Play/Pause" />
    </button>
    <div></div>
</div>

<style>
    .play-button {
        width: 25px;
        height: 25px;
        transition: all .5s;
    }
    .play-button:hover {
        cursor: pointer;
        filter: brightness(.7);
        transition: all .5s;
    }
    .play-button:active {
        transform: translateY(3px);
        transition: none;
    }
    button {
        background-color: transparent;
        border: none;
    }
    button:active {
        background-color: transparent;
        border: none;
    }
</style>
