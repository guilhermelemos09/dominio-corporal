const CACHE_NAME = 'dominio-corporal-v98';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './treino.html',
  './manifest.json',
  './Midia/icon-192.png',
  './Midia/icon-512.png',
  './Midia/icon-pessoal-192.png',
  './Midia/icon-pessoal-512.png',
  './Midia/favicon.png',
  './Midia/icon_evol_composicao.png',
  './Midia/icon_evol_tecnica.png',
  './Midia/icon_evol_recordes.png',
  './Midia/icon_evol_relatorio.png',
  './helenice.html',
  './manifest-helenice.json',
  'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
];

// Install: precache app shell
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }).then(() => self.skipWaiting())
  );
});

// Activate: clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: network first with offline fallback for html, cache first for fonts e midias
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);

  // If requesting video, use normal browser streaming (do not cache large mp4)
  if (url.pathname.endsWith('.mp4')) {
    return;
  }

  // Network-first strategy for app files so Gui always gets latest training updates
  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const responseClone = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseClone);
          });
        }
        return networkResponse;
      })
      .catch(() => {
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          if (event.request.headers.get('accept')?.includes('text/html')) {
            return caches.match('./index.html');
          }
        });
      })
  );
});
