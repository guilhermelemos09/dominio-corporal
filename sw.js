const CACHE_NAME = 'dominio-corporal-v6';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './treino.html',
  './demo_treino_completo.html',
  './aluno.html',
  './demo_treino_branco.html',
  './icon-192.png',
  './icon-512.png',
  './icon-pessoal-192.png',
  './icon-pessoal-512.png',
  './favicon.png',
  './manifest.json',
  './manifest-pessoal.json',
  './manifest-aluno.json',
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

// Fetch: network first with offline fallback for html, cache first for fonts
self.addEventListener('fetch', (event) => {
  // Ignore non-GET requests
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
          if (event.request.headers.get('accept')?.includes('text/html')) {
            return caches.match('./index.html');
          }
        });
      })
  );
});
