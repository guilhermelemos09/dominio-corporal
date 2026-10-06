const CACHE_NAME = 'dominio-corporal-v38';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './treino.html',
  './jean.html',
  './manifest-jean.json',
  './icon-192.png',
  './icon-512.png',
  './icon-pessoal-192.png',
  './icon-pessoal-512.png',
  './favicon.png',
  './gui_foto.jpg',
  './Midia/comparacao_frontal_relaxado.jpg',
  './Midia/comparacao_duplo_biceps.jpg',
  './manifest.json',
  './manifest-pessoal.json'
];

// Install: precache app shell safely without failing on network/font issues
self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return Promise.allSettled(
        ASSETS_TO_CACHE.map((url) =>
          cache.add(url).catch((err) => console.warn('Cache fallback for ' + url, err))
        )
      );
    })
  );
});

// Activate: clean up old caches immediately and take control
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('Purging legacy cache:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: network first with offline fallback for html, cache first for fonts
self.addEventListener('fetch', (event) => {
  // Ignore non-GET requests
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);

  // If requesting video, use normal browser streaming (do not cache large mp4)
  if (url.pathname.endsWith('.mp4')) {
    return;
  }

  const isHtml = event.request.mode === 'navigate' || event.request.headers.get('accept')?.includes('text/html');

  // Network-first strategy for app files so Gui always gets latest training updates
  event.respondWith(
    (isHtml ? fetch(event.request, { cache: 'reload' }) : fetch(event.request))
      .then((networkResponse) => {
        // Clone and cache the fresh response
        if (networkResponse && networkResponse.status === 200) {
          const responseClone = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseClone);
          });
        }
        return networkResponse;
      })
      .catch(() => {
        // Fallback to cache if offline
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          if (isHtml) {
            return caches.match('./index.html');
          }
        });
      })
  );
});
