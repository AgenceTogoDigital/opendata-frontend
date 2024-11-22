import { create } from '@storybook/theming/create';
import logo from '../../../templates/svg/logotype.svg';

export default create({
  base: 'light',
  // Typography
  fontBase: 'Marianne, sans-serif',
  fontCode: 'monospace',

  brandTitle: 'opendata.gouv.tg Storybook',
  brandUrl: 'https://www.opendata.gouv.tg',
  brandImage: logo,
  colorPrimary: '#161616',
  colorSecondary: '#3558a2'
});
