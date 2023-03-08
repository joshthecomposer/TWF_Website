<div class="header">
    <h1>
        MEET THE TEAM
    </h1>
    <h2>
        A podcast forged in friendship
    </h2>
    <hr>
    <div class="blurb">
        <p>Founded and co-hosted by Andie, Tolkien with Friends was created to capture the conversations only best friends can have: silly, thoughtful, and serious all at once — and always about the things those friends are passionate about.</p>
        <br/>
        <p>In our case, that’s the works of J.R.R. Tolkien, the Lord of the Rings movies, and fantasy in general. What started as a shared journey with two best friends comparing and contrasting the Lord of the Rings books and movies has since expanded to include a more friends and, really, a whole community of Tolkien fans.</p>
    </div>
    <hr>
</div>
<div class="container">
    <img class="prof-pic" src="./img/andie.jpg" alt="">
    <div class="bio">
        <h3>
            Andie
        </h3>
        <p>What started as a series on her TikTok quickly became a passion project because Andie simply has too much to say about Lord of the Rings. Instead of simply revealing “Lines from Lord of the Rings” she wished had been in the movies, she started a podcast with the goal of comparing the books and the movies chapter by chapter and scene by scene, turning her yearly re-read into a year-long project – and now a project with no end date 😜
        </p>
    </div>
    <img class="prof-pic" src="./img/kali.JPG" alt="">
    <div class="bio">
        <h3>
            Kali
        </h3>
        <p>Kali is a cosplayer, content creator, and community organizer in the Tolkien fan space. After joining Tolkien with Friends partway through the first season, Kali adds a thoughtful perspective to every episode. Kali is also a cohost of the Voices of Arda podcast with KnewBettaDoBetta, which gives another unique spin on all things Tolkien.
        </p>
    </div>
    <img class="prof-pic" src="./img/ahnna2.jpeg" alt="">
    <div class="bio">
        <h3>
            Ahnna
        </h3>
        <p>Andie’s best friend and a huge Game of Thrones fan, Ahnna helped add a movies-only fan perspective to keep Andie’s rants in check. Always ready to reference George R.R. Martin, Ahnna loaned us her magical brain up until the birth of her perfect baby boy. We’re keeping our fingers crossed for a comeback!
        </p>
    </div>
</div>

<style>
    * {
        letter-spacing: normal;
    }
    h1 {
        font-family: "Oswald";
        color: #2D2D2D;
        font-weight: 500;
        font-size: 6.0rem;
        margin-top: 4rem;
        letter-spacing: normal;
        text-transform: uppercase;
        text-align: center;
    }
    .container {
        display: grid;
        padding: 5rem;
        grid-template-columns: 1fr 1fr;
        background-color: #83967D;
        row-gap: 5rem;
    }

    .prof-pic {
        grid-column-start: 1;
        align-self: center;
        justify-self: flex-end;
        height: 250px;
        border-radius: 50%;
        box-shadow: 0px 3px 15px rgba(0,0,0,0.2);
        margin-right: 20rem;

    }
    .bio {
        display: flex;
        flex-direction: column;
        gap: 2rem;
        grid-column-start: 2;
        align-self: center;
        justify-self: start;
    }
    p {
        font-size: 1.8rem;
        color: #2D2D2D;
        font-weight: 500;
        letter-spacing: 2.5px;
    }

    h2 {
        color: #2D2D2D;
        text-align: center;
        margin-top: 2rem;
        text-transform: uppercase;
    }
    h3 {
        font-size: 2.8rem;
        color: #2D2D2D;
        margin-top: 2rem;
        text-transform: uppercase;
    }
    .header {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .blurb {
        max-width: 50%;
        text-align: center;
    }
    .blurb p {
        font-weight: 800;
        letter-spacing: 2.8px;
    }
    hr {
        border-top: 2px solid #2D2D2D;
        width: 45%;
        text-align: center;
        margin: 4rem 0 4rem 0;
    }
</style>
