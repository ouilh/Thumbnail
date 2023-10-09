document.addEventListener("DOMContentLoaded", function () {
    const videoUrlInput = document.getElementById("videoUrlInput");
    const getThumbnailBtn = document.getElementById("getThumbnailBtn");
    const thumbnailContainer = document.getElementById("thumbnailContainer");

    getThumbnailBtn.addEventListener("click", () => {
        const youtubeUrl = videoUrlInput.value;
        const videoId = extractVideoId(youtubeUrl);
        const button = document.getElementById("getThumbnailBtn"); 
        const submit = document.getElementById("dis"); 

        if (videoId) {
            const thumbnailUrl = `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`;
                        button.style.display = "none";
                        submit.style.display = "block"
           
            thumbnailContainer.innerHTML = `<img class="shadow" src="${thumbnailUrl}" alt="Video Thumbnail">`;
        } else {
            thumbnailContainer.innerHTML = "Invalid YouTube URL";
        }
    });

    // Function to extract video ID from YouTube URL
    function extractVideoId(url) {
        const videoIdMatch = url.match(/(?:\?v=|\/embed\/|\/watch\?v=|\/v\/|youtu\.be\/|\/embed\/|\/e\/|watch\?v=|v\/)([^#\&\?]*).*/i);
        return videoIdMatch && videoIdMatch[1];
    }
});
