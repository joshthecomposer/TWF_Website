<script>
    import AP from "./AudioPlayer.svelte";
    async function getPodcasts() {
        const response = await fetch("http://localhost:5000/api/episodes");
        const data = await response.json();
        if (response.ok){
            return data;
        } else {
            throw new Error(data);
        }
    } 
    let promise = getPodcasts();
</script>

<div class="episodes">
    {#await promise then podcasts}
        {#each podcasts as podcast}
            <div class="podcast">
                <p>{podcast.title}</p>
                <AP src={podcast.links[0].href}/>
            </div>
        {/each}
    {/await}
</div>

<style>
    .episodes {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>
