<script>
    import {fade, slide, fly} from "svelte/transition";
    import { Link } from "svelte-navigator";
    import AP from "./AudioPlayer.svelte";
    async function getLatest() {
        const response = await fetch("http://localhost:5000/api/episodes/latest")
        const data = await response.json();
        if (response.ok){
            const title = data.title.split(":")
            data[0] = title;
            return data;
        } else {
            throw new Error(data);
        }
    } 
    console.log(getLatest());
    let promise = getLatest();
</script>

<div class="container-1">
    <h1 in:fly={{x:-200, duration: 1000, delay: 250}}>Latest Episode</h1>
    <div in:fly={{x:200 , duration: 1000, delay: 250}} class="podcast">
        {#await promise then latest}
            <h2><span class="ep-no">{latest[0][0]} : </span>{latest[0][1]}</h2>
            <AP src={latest.links[0].href}/>
        {/await}
    </div>
    <img class="hill-2" src="./img/hill 2.svg" alt="">
</div>

<div class="container-2">
    <div class="blurb">
        <hr>
        <p class="pblurb">Join Andie, Kali and friends as they re-discover Middle-earth together by comparing the works of Tolkien to their various adaptations, starting with Peter Jackson's take on <i>Lord of the Rings</i> and <i>The Hobbit</i>.</p>
        <hr>
        <Link style="text-decoration: none;"to="about"><p class="more">MORE ABOUT US</p></Link>
    </div>
</div>

<div class="diag"></div>

<div class="container-3">
    <div class="card">
        <h3 class="card-header">Merchandise</h3>
        <a rel="noreferrer" href="https://tolkien-with-friends-shop.creator-spring.com/" target="_blank">
            <img class="thumbnail" src="./img/spring.png" alt="Merch" />
        </a>
    </div>
    <div class="card">
        <h3 class="card-header">Patreon</h3>
        <a rel="noreferrer" href="https://www.patreon.com/TolkienwithFriends" target="_blank">
            <img class="thumbnail" src="./img/patreonprev.png" alt="Patreon" />
        </a>
    </div>
    <div class="card">
        <h3 class="card-header">Discord</h3>
        <a rel="noreferrer" href="https://discord.com/invite/PDqRa7mamJ" target="_blank">
            <img class="thumbnail" src="./img/discord.png" alt="Discord" />
        </a>
    </div>
</div>

<div class="diag-3"></div>

<div class="container-4">
    <div class="footer">
        <p>© 2023 Tolkien With Friends Podcast | Website Designed by <a href="/">JoshTheComposer</a></p>
    </div>
</div>

<style>
    h1 {
        font-family: "Oswald";
        color: #2D2D2D;
        font-weight: 500;
        font-size: 6.0rem;
        letter-spacing: normal;
        text-transform: uppercase;
        margin-top: 5rem;
    }
    h2 {
        font-style: italic;
        letter-spacing: 0;
        color: rgb(193, 193, 193);
        font-weight: 300;
        font-size: 20px;
    }
    .ep-no {
        font-style: normal;
        font-weight: 500;
        font-size: 21px;
        color: white;
    }
    .hill-2 {
        justify-self: start;
    }
    .container-1 {
        display: flex;
        flex-direction: column;
        gap: 3rem;
        align-items: center;
        background-color: #83967D;
    }

    .container-2 {
        display: flex;
        flex-direction: column;
        gap: 3rem;
        align-items: center;
        background-color: #546142;
    }
    .blurb {
        display: flex;
        flex-direction: column;
        gap: 2rem;
        align-items: center;
        text-align: center;
        max-width: 66.06rem;
        /* box-shadow: 0px 3px 15px rgba(0,0,0,0.2);   */
        padding: 0 2rem 2rem 2rem;  
        border-radius: 5px;
        margin-bottom: 5rem;
    }
    hr {
        border-top: 1px solid white;
        width: 75%;
        text-align: center;
    }
    .pblurb {
        color: white;
        letter-spacing: 1px;
        /* font-weight: ; */
        font-size: 2.0rem;
    }

    .more {
        color: white;
        text-decoration: none;
        border: 1px solid white;
        border-radius: 5px;
        padding: 1.5rem 2rem 1.5rem 2rem;
        background-color: transparent;
        transition: all 1s;
    }
    .more:hover {
        transition: all 1s;
        color: #546142;
        background-color: white;
    }
    .more:active {
        transform: translateY(3px);
    }
    .container-3{
        background-color: #83967D;
        display: flex;
        gap: 10rem;
        justify-content: center;
        padding: 0 5rem 0 5rem;
        margin: 5rem 0 5rem 0;

    }
    .card {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 3rem;
        width: 300px;
        height: 400px;
        box-shadow: 0px 3px 15px rgba(0,0,0,0.2);
        border-radius: 5px;
        background-color:#b7c2b3;
        gap: 3rem;
    }

    .diag {
        margin: 0;
        max-width: 100%;
        border-left: 99vw solid transparent;
        border-top: 5vw solid #546142;
        /* margin-top: -13.9vw; */
    }
    .diag-3 {
        margin: 0;
        max-width: 100%;
        border-right: 99vw solid transparent;
        border-bottom: 5vw solid #3C4B37;
        /* margin-top: -13.9vw; */
    }

    .card-header {
        font-family: 'Oswald';
        color: #2D2D2D;
        font-size: 2.4rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 5px;
    }
    .thumbnail {
        border-radius: 5px;
        width: 100%;
        box-shadow: 0px 3px 15px rgba(0,0,0,0.2);
        opacity: 80%;
        transition: all 500ms;
    }

    .thumbnail:hover {
        transform: scale(105%);
        transition: all 500ms;
    }

    .container-4 {
        background-color: #3C4B37;
        height: 100%;
        padding: 0 0 2rem 0;
    }

    .footer {
        display: flex;
        justify-content: center;
        letter-spacing: normal;
    }
    .footer a {
        color: white;
        text-decoration: underline;

    }

</style>