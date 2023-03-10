<script>
    async function getBlogs() {
        const response = await fetch("/api/blogs");
        const data = await response.json();
        if (response.ok){
            return data;
        } else {
            throw new Error(data);
        }
    } 
    let promise = getBlogs();
</script>

<div>
    {#await promise then blogs}
        {#each blogs as blog}
            <div class="blog">
                <p>{blog.title}</p>
            </div>
        {/each}
    {/await}
</div>

<style>
    .blog {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>