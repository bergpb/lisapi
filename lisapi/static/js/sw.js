console.log('Hello from sw.js');

importScripts('https://storage.googleapis.com/workbox-cdn/releases/3.4.1/workbox-sw.js');

if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);

  workbox.precaching.precacheAndRoute([
    {
      "url": "/",
      "revision": "aff2df68"
    },
    {
      "url": "/login",
      "revision": "aff2df68"
    },
    {
      "url": "/change_password",
      "revision": "aff2df68"
    },
    {
      "url": "/create",
      "revision": "aff2df68"
    },
    {
      "url": "/list",
      "revision": "aff2df68"
    },
    {
      "url": "/edit",
      "revision": "aff2df68"
    },
    {
      "url": "/control",
      "revision": "aff2df68"
    },
    {
      "url": "/about",
      "revision": "aff2df68"
    }
  ]);

  workbox.routing.registerRoute(
    /\.(?:js|css)$/,
    workbox.strategies.networkFirst({
      cacheName: 'lisapi-static-resources',
    }),
  );

  workbox.routing.registerRoute(
    /\.(?:png|gif|jpg|jpeg|svg)$/,
    workbox.strategies.staleWhileRevalidate({
      cacheName: 'lisapi-images',
      plugins: [
        new workbox.expiration.Plugin({
          maxEntries: 60,
          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
        }),
      ],
    }),
  );

  workbox.routing.registerRoute(
    new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
    workbox.strategies.staleWhileRevalidate({
      cacheName: 'lisapi-googleapis',
      plugins: [
        new workbox.expiration.Plugin({
          maxEntries: 30,
        }),
      ],
    }),
  );

} else {
  console.log(`Boo! Workbox didn't load 😬`);
}