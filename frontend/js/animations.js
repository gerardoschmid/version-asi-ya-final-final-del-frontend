/*
    ==============================================
    ANIMATIONS.JS
    ==============================================
*/

document.addEventListener('DOMContentLoaded', () => {
    // --- Animación de entrada para secciones ---
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Seleccionamos elementos que queremos animar
    const elementsToAnimate = document.querySelectorAll('.habitacion_tarjeta, .seccion_busqueda, .contenedor_detalle > *, .subtitulo');

    elementsToAnimate.forEach(el => {
        // Establecemos un estado inicial para la animación
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(el);
    });

    // --- Efecto de brillo en hover para botones ---
    const buttons = document.querySelectorAll('.boton_principal, .boton_fullwidth');

    buttons.forEach(button => {
        button.addEventListener('mouseenter', (e) => {
            // Creamos el elemento span para el brillo
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');

            const rect = button.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = `${size}px`;
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;

            // Añadimos el ripple y lo eliminamos después de la animación
            button.appendChild(ripple);
            setTimeout(() => {
                ripple.remove();
            }, 600); // Coincide con la duración de la animación en CSS
        });
    });

    // --- Añadimos el CSS necesario para el efecto ripple ---
    const style = document.createElement('style');
    style.innerHTML = `
        .boton_principal, .boton_fullwidth {
            position: relative;
            overflow: hidden;
        }

        .ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.4);
            transform: scale(0);
            animation: ripple-effect 0.6s linear;
        }

        @keyframes ripple-effect {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
});
