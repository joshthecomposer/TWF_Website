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

<div class="blog-con">
    <h1>Blogs</h1>
    <hr>
    {#await promise then blogs}
        {#each blogs as b}
            <div class="blog">
                <h2>{b.title}</h2>
                <p class="author"><em>by {b.author}</em></p>
                <br>
                {#each b.blocks as c}
                    <p class="content" style="white-space: pre-line">{c.text}</p>
                    <br>
                {/each}
                <p class="published"><em>published on {b.updated_at}</em></p>
            </div>
        {/each}
    {/await}
</div>

<style>
    h1 {
        font-family: "Oswald";
        color: #2D2D2D;
        font-weight: 500;
        font-size: 6.0rem;
        margin-top: 4rem;
        letter-spacing: normal;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 4rem;
    }
    h2 {
        font-family: "Oswald";
        font-weight: 500;
        font-size: 4.8rem;
        color: #2D2D2D;
        letter-spacing: normal;
        text-transform: uppercase;
    }
    .author {
        letter-spacing: normal;
        font-weight: 300;
        color: #2D2D2D;
    }
    .published {
        letter-spacing: normal;
        font-weight: 300;
        color: #2D2D2D;
    }
    .blog {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        max-width: 75rem;
        box-shadow: 0px 3px 15px rgba(0,0,0,0.2);
        padding: 3rem;
        background-color:#b7c2b3;
        border-radius: 15px;
    }
    .blog-con {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 5rem;
    }
    .content {
        letter-spacing: normal;
        font-size: 1.8rem;
        color: #2D2D2D;
        font-weight: 500;
    }
    hr {
        border-top: 2px solid #2D2D2D;
        width: 45%;
        text-align: center;
        margin: 4rem 0 4rem 0;
    }
</style>