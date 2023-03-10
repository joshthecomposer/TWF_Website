<script>
    import { Link } from "svelte-navigator";
</script>
<div class="sub-nav">
    <ul class="icon-list">
        <li>
            <a href="patreon.com">
                <img class="soc-icon" src="img/patreon.png" alt="">
            </a>
        </li>
        <li>
            <a href="discord.com">
                <img class="soc-icon" src="img/discord.webp" alt="">
            </a>
        </li>
        <li>
            <a href="instagram.com">
                <img class="soc-icon" src="img/insta.webp" alt="">
            </a>
        </li>
        <li>
            <a href="youtube.com">
                <img class="soc-icon" src="img/youtube.webp" alt="">
            </a>
        </li>
        <li>
            <a href="twitter.com">
                <img class="soc-icon" src="img/twitter.webp" alt="">
            </a>
        </li>
    </ul>
</div>
<nav>
    <ul>
        <li>
            <Link class="nav-link" to="about">About</Link>
        </li>
        <li>
            <Link class="nav-link" to="episodes">Episodes</Link>
        </li>
        <li>
            <a rel="noreferrer" target="_blank" class="nav-link" href="https://tolkien-with-friends-shop.creator-spring.com/">Merch</a>
        </li>
        <li>
            <Link to="/"><img class="main-logo nav-link" src="img/BIGGGG-01.png" alt="Tolkien with Friends"></Link>
        </li>
        <li>
            <Link class="nav-link" to="blog">Blogs</Link>
        </li>
        <li>
            <Link class="nav-link" to="subscribe">Subscribe</Link>
        </li>
        <li>
            <Link class="nav-link" to="contact">Contact</Link>
        </li>
    </ul>
</nav>
<!-- <div class="mountains">
    <img src="img/hill 1.svg" alt="">
</div> -->

<style>
    @media all and (max-width: 1055px) {
        nav {
            display: none !important;
        }
    }
    nav {
        display: flex;
        flex-direction: column;
        /* justify-content: center; */
        align-items: center;
        background-color: #3C4B37;
        /* transform: translateY(-50px); */
        margin-top: -40px;

    }
    ul {
        display: flex;
        gap: 40px;
        align-items: center;
    }
    li {
        color: white;
        list-style-type: none;
        
    }
    .main-logo {
        height: 300px;
    }

    .sub-nav {
        display: flex;
        gap: 30px;
        align-items: center;
        justify-content: flex-end;
        background-color: #3C4B37;
    }

    .soc-icon {
        height: 20px;
    }
    .soc-icon:hover {
        filter: color(black);
    }

    .icon-list {
        margin-top: 15px;
        margin-right: 30px;
    }
    /* .mountains {
        width: 100%;
        background-color:#3C4B37;
    } */


</style>
