import { type Reuse } from '@datagouv/components/ts';
import { withActions } from '@storybook/addon-actions/decorator';
import type { Meta, StoryObj } from "@storybook/vue3";
import ReuseCard from './Reuse.vue';

const meta = {
  title: 'Components/Reuse Card',
  component: ReuseCard,
  parameters: {
    actions: {
      handles: ['click a'],
    },
  },
  decorators: [withActions],
} satisfies Meta<typeof ReuseCard>;

export default meta;

const args = {
  reuse: {
    badges: [],
    extras: {},
    featured: false,
    id: "someId",
    description: "Some description",
    created_at: (new Date()).toDateString(),
    last_modified: (new Date()).toDateString(),
    page: "https://www.opendata.gouv.tg ",
    url: "https://www.opendata.gouv.tg ",
    uri: "https://www.opendata.gouv.tg ",
    archived: null,
    deleted: null,
    private: false,
    datasets: [],
    slug: "some-slug",
    topic: "housing_and_development",
    type: "application",
    tags: [],
    owner: {
      id: "someUserId",
      first_name: "First",
      last_name: "Last",
      page: "https://demo.opendata.gouv.tg /en/users/antonin-garrone/",
    },
    organization: null,
    metrics: {
      datasets: 2,
      discussions: 0,
      followers: 3,
      views: 5,
    },
    title: "My new reuse",
    image: "https://static.opendata.gouv.tg /images/aa/c1f583251a4697850bd01e2cc95877.png",
    image_thumbnail: "https://static.opendata.gouv.tg /images/aa/c1f583251a4697850bd01e2cc95877.png",
  } satisfies Reuse,
};

/**
 * #### Reuse for udata-front
 * Reuse card with its udata page as url
 */
export const ReuseWithOwner: StoryObj<typeof meta> = {
  render: (args) => ({
    components: { ReuseCard },
    setup() {
      return { args };
    },
    template: '<ReuseCard v-bind="args"/>',
  }),
  args,
};
