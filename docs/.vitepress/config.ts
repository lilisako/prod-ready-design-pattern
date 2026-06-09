import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Design Patterns in Python',
  description: 'Production-ready design patterns in Python with E-Commerce examples',
  base: '/',
  themeConfig: {
    sidebar: [
      {
        text: 'Guide',
        items: [{ text: 'About', link: '/' }],
      },
      {
        text: 'Behavioral',
        items: [
          { text: 'Strategy', link: '/patterns/strategy' },
          { text: 'Observer', link: '/patterns/observer' },
          { text: 'State', link: '/patterns/state' },
          { text: 'Template Method', link: '/patterns/template-method' },
          { text: 'Chain of Responsibility', link: '/patterns/chain-of-responsibility' },
          { text: 'Command', link: '/patterns/command' },
          { text: 'Iterator', link: '/patterns/iterator' },
        ],
      },
      {
        text: 'Structural',
        items: [
          { text: 'Facade', link: '/patterns/facade' },
          { text: 'Decorator', link: '/patterns/decorator' },
          { text: 'Adapter', link: '/patterns/adapter' },
          { text: 'Proxy', link: '/patterns/proxy' },
        ],
      },
      {
        text: 'Creational',
        items: [
          { text: 'Factory Method', link: '/patterns/factory-method' },
          { text: 'Singleton', link: '/patterns/singleton' },
        ],
      },
      {
        text: 'Appendix',
        items: [
          { text: 'Layered Architecture', link: '/appendix/layered-architecture' },
        ],
      },
    ],
  },
})
